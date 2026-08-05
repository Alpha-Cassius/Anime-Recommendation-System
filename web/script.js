document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    const loadingDiv = document.getElementById('loading');
    const messageDiv = document.getElementById('message');
    const resultsGrid = document.getElementById('results-grid');
    const autocompleteList = document.getElementById('autocomplete-list');
    let debounceTimer;

    async function handleSearch() {
        const query = searchInput.value.trim();
        if (!query) return;

        // UI Reset
        resultsGrid.innerHTML = '';
        resultsGrid.classList.add('hidden');
        messageDiv.classList.add('hidden');
        loadingDiv.classList.remove('hidden');

        try {
            // Call Python function via Eel
            const response = await eel.recommend(query)();
            
            loadingDiv.classList.add('hidden');

            if (response.success) {
                const results = response.data;
                
                if (results.length === 0) {
                    showMessage(`No recommendations found for "${query}". Try another anime!`);
                } else {
                    renderResults(results);
                }
            } else {
                showMessage(`An error occurred: ${response.error}`);
            }
        } catch (err) {
            loadingDiv.classList.add('hidden');
            showMessage('Failed to communicate with the heavens (Server error).');
            console.error(err);
        }
    }

    function showMessage(msg) {
        messageDiv.textContent = msg;
        messageDiv.classList.remove('hidden');
    }

    function renderResults(results) {
        resultsGrid.classList.remove('hidden');
        
        results.forEach((anime, index) => {
            const card = document.createElement('div');
            card.className = 'card';
            // Stagger animations
            card.style.animationDelay = `${index * 0.05}s`;

            // Split genres and create tags (handle potential empty string)
            const genres = anime.genre ? anime.genre.split(',').map(g => g.trim()) : [];
            const genreHtml = genres.slice(0, 4).map(g => `<span class="genre-tag">${g}</span>`).join('');
            const typeInfo = anime.type || 'Unknown';
            const epInfo = anime.episodes !== 'Unknown' ? `${anime.episodes} ep` : '';

            card.innerHTML = `
                <div class="card-title" title="${anime.name}">${anime.name}</div>
                <div class="card-meta">
                    <span class="type">${typeInfo} ${epInfo ? '• ' + epInfo : ''}</span>
                    <span class="rating">★ ${anime.rating > 0 ? anime.rating : 'N/A'}</span>
                </div>
                <div class="card-genres">
                    ${genreHtml}
                </div>
                <a href="https://myanimelist.net/anime/${anime.anime_id}" target="_blank" rel="noopener noreferrer" class="mal-btn">
                    View on MyAnimeList
                </a>
            `;
            
            resultsGrid.appendChild(card);
        });
    }

    searchBtn.addEventListener('click', () => {
        autocompleteList.classList.add('hidden');
        handleSearch();
    });
    
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            autocompleteList.classList.add('hidden');
            handleSearch();
        }
    });

    searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        const query = e.target.value.trim();
        
        if (!query) {
            autocompleteList.innerHTML = '';
            autocompleteList.classList.add('hidden');
            return;
        }

        debounceTimer = setTimeout(async () => {
            try {
                const response = await eel.search_suggestions(query)();
                if (response.success && response.data.length > 0) {
                    autocompleteList.innerHTML = '';
                    response.data.forEach(title => {
                        const div = document.createElement('div');
                        div.innerText = title;
                        div.addEventListener('click', () => {
                            searchInput.value = title;
                            autocompleteList.classList.add('hidden');
                            handleSearch();
                        });
                        autocompleteList.appendChild(div);
                    });
                    autocompleteList.classList.remove('hidden');
                } else {
                    autocompleteList.classList.add('hidden');
                }
            } catch (err) {
                console.error(err);
            }
        }, 300);
    });

    // Close autocomplete when clicking outside
    document.addEventListener('click', (e) => {
        if (e.target !== searchInput && e.target !== autocompleteList) {
            autocompleteList.classList.add('hidden');
        }
    });
});
