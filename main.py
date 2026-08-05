import eel
from recommender import get_recommendations
import os

# Initialize eel with the web folder
base_path = os.path.dirname(os.path.abspath(__file__))
web_folder = os.path.join(base_path, 'web')
eel.init(web_folder)

@eel.expose
def recommend(title):
    """
    Exposed function for Javascript to call.
    Gets recommendations based on the anime title.
    """
    try:
        results = get_recommendations(title)
        return {"success": True, "data": results}
    except Exception as e:
        return {"success": False, "error": str(e)}

@eel.expose
def search_suggestions(query):
    from recommender import search_anime
    try:
        results = search_anime(query)
        return {"success": True, "data": results}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == '__main__':
    # Start the eel app
    try:
        eel.start('index.html', size=(1200, 800), mode='chrome')
    except Exception as e:
        # Fallback to default browser if Chrome is not found
        eel.start('index.html', size=(1200, 800), mode='default')
