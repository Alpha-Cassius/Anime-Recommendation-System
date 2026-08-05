# Celestial Anime Recommendation System

A heavenly, beautifully designed desktop-like application that provides intelligent anime recommendations based on a content-filtering TF-IDF algorithm. Built entirely with **Python, Eel, HTML, CSS, and Vanilla JavaScript**, it features a premium glassmorphism design, live search autocomplete, and direct integrations with MyAnimeList.

## 🌟 Features
- **Intelligent Recommendations**: Uses TF-IDF vectorization on anime genres to find similarities and sorts by popularity and ratings using `pandas` and `scikit-learn`.
- **Live Search Autocomplete**: As you type, the system instantly fetches matching anime from the dataset and displays them in a sleek dropdown.
- **MyAnimeList Integration**: Every recommendation provides a direct link to the official MyAnimeList page.
- **Premium UI/UX**: "Heavenly" aesthetic with floating orbs, glassmorphism UI components, smooth entrance animations, and micro-interactions.
- **Desktop-Like Experience**: Powered by the Python `eel` library, the app opens as a standalone window.

## 🛠️ Technologies Used
- **Backend**: Python 3, `pandas`, `scikit-learn`, `eel`
- **Frontend**: HTML5, Vanilla CSS (CSS variables, flexbox/grid, animations), Vanilla JavaScript (ES6+, async/await)

## 🚀 How to Run

1. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install eel pandas scikit-learn
   ```

2. **Run the Application**:
   Navigate to the project folder and run `main.py`:
   ```bash
   python main.py
   ```
   A new window will open automatically.

## 📂 Project Structure
- `main.py`: The entry point that sets up the Eel server and exposes Python functions.
- `recommender.py`: Data loading, TF-IDF algorithm, and search suggestion logic.
- `web/`: The frontend folder containing `index.html`, `style.css`, and `script.js`.
- `anime.csv`: The dataset containing anime details and genres.

---

Made with 💖 and ☕ by Vaibhav Pandey!