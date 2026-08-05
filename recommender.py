import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os
import difflib

# Load the dataset
# Assuming anime.csv is in the same directory as this script
base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, 'anime.csv')

df = pd.read_csv(csv_path)

# Handle missing values
df['genre'] = df['genre'].fillna('')
df['rating'] = df['rating'].fillna(0.0)

# Create a TF-IDF matrix for genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create a reverse map of indices and anime titles
# Using lower case to allow case-insensitive search
df['name_lower'] = df['name'].str.lower()
indices = pd.Series(df.index, index=df['name_lower']).drop_duplicates()

def get_recommendations(title, top_n=12):
    title_lower = title.lower()
    title_no_spaces = title_lower.replace(' ', '')
    df['name_no_spaces'] = df['name_lower'].str.replace(' ', '')
    
    idx = None
    
    # 1. Exact match
    if title_lower in indices:
        idx = indices[title_lower]
        if isinstance(idx, pd.Series): idx = idx.iloc[0]
    else:
        # 2. Contains match (space-insensitive)
        partial_matches = df[df['name_no_spaces'].str.contains(title_no_spaces, na=False)]
        if not partial_matches.empty:
            idx = partial_matches.sort_values(by='members', ascending=False).index[0]
        else:
            # 3. Fuzzy matching
            all_names = df['name_lower'].tolist()
            close_matches = difflib.get_close_matches(title_lower, all_names, n=1, cutoff=0.4)
            if close_matches:
                best_match = close_matches[0]
                idx = indices[best_match]
                if isinstance(idx, pd.Series): idx = idx.iloc[0]
                
    if idx is None:
        return []

    # Get the pairwise similarity scores of all anime with that anime
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the anime based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 50 most similar anime
    sim_scores = sim_scores[1:51]

    # Get the anime indices
    anime_indices = [i[0] for i in sim_scores]

    # Get the top 50 similar anime
    similar_anime = df.iloc[anime_indices].copy()
    
    # Sort these top 50 by rating and then by popularity (members)
    similar_anime = similar_anime.sort_values(by=['rating', 'members'], ascending=[False, False])
    
    # Get the top N
    top_anime = similar_anime.head(top_n)
    
    # Format the output
    results = []
    for _, row in top_anime.iterrows():
        results.append({
            'anime_id': int(row['anime_id']),
            'name': row['name'],
            'genre': row['genre'],
            'type': row['type'],
            'episodes': row['episodes'],
            'rating': row['rating'],
            'members': row['members']
        })
        
    return results

def search_anime(query, limit=5):
    """
    Returns a list of anime names that match the query for autocomplete.
    Uses space-insensitive search and fuzzy matching.
    """
    if not query:
        return []
    
    query_lower = query.lower()
    query_no_spaces = query_lower.replace(' ', '')
    df['name_no_spaces'] = df['name_lower'].str.replace(' ', '')
    
    # 1. Contains match (space-insensitive)
    matches = df[df['name_no_spaces'].str.contains(query_no_spaces, na=False)]
    
    # 2. Fuzzy matching if no contains matches
    if matches.empty:
        all_names = df['name_lower'].tolist()
        close_matches = difflib.get_close_matches(query_lower, all_names, n=limit, cutoff=0.4)
        if close_matches:
            matches = df[df['name_lower'].isin(close_matches)]
            
    if not matches.empty:
        # Sort matches by members to show popular anime first
        matches = matches.sort_values(by='members', ascending=False)
        return matches.head(limit)['name'].tolist()
        
    return []

if __name__ == "__main__":
    # Test
    print(get_recommendations("Kimi no Na wa."))
