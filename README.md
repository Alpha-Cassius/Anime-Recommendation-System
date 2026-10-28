<div align="center">

# 🌌 Celestial Anime Recommendation System

**A heavenly, desktop-like application providing intelligent anime recommendations based on a TF-IDF content-filtering algorithm.**

<p>
<a href="https://github.com/alpha-cassius"><img src="https://img.shields.io/badge/AUTHOR-Vaibhav_Pandey-8a2be2?style=for-the-badge&amp;labelColor=0d1117" alt="AUTHOR" /></a> 
<a href="https://github.com/alpha-cassius?tab=repositories"><img src="https://img.shields.io/badge/OPEN_SOURCE-00d2ff?style=for-the-badge&amp;labelColor=0d1117" alt="OPEN SOURCE" /></a> 
<img src="https://img.shields.io/badge/UI/UX-GLASSMORPHISM-a8c0ff?style=for-the-badge&amp;labelColor=0d1117" alt="UI/UX" />
</p>

<p><b>Built entirely with Python, Eel, HTML, CSS, and Vanilla JavaScript.</b></p>

---

</div>

## ✨ About The Project

The **Celestial Anime Recommendation System** brings a premium, desktop-like experience to discovering your next favorite anime. By blending a beautiful **glassmorphism UI** with a powerful **Machine Learning backend**, this application calculates similarities between anime genres and presents them in a sleek, standalone window.

<br/>

## 🌟 Core Features

<table width="100%">
<tr>
<td width="50%" valign="top">
  <h3>🧠 Intelligent Recommendations</h3>
  <p>Uses <b>TF-IDF vectorization</b> on anime genres to find similarities, sorting the results by popularity and ratings using <code>pandas</code> and <code>scikit-learn</code>.</p>
</td>
<td width="50%" valign="top">
  <h3>⚡ Live Search Autocomplete</h3>
  <p>As you type, the system instantly fetches matching anime from the dataset and displays them in a sleek dropdown menu without refreshing.</p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <h3>🔗 MyAnimeList Integration</h3>
  <p>Every generated recommendation provides a direct link to the official <b>MyAnimeList</b> page so you can instantly add it to your watchlist.</p>
</td>
<td width="50%" valign="top">
  <h3>🔮 Premium UI & Desktop Feel</h3>
  <p>Features a "Heavenly" aesthetic with floating orbs, glassmorphism components, and smooth animations, all opening as a native desktop window powered by <code>eel</code>.</p>
</td>
</tr>
</table>

<br/>

## 🛠️ Technologies Used

| Stack | Technologies |
| :--- | :--- |
| **Backend** | Python 3 · `pandas` · `scikit-learn` · `eel` |
| **Frontend** | HTML5 · Vanilla CSS *(Custom variables, flexbox, animations)* · Vanilla JavaScript *(ES6+, async/await)* |
| **Data** | Kaggle/MAL Dataset (`anime.csv`) |

<br/>

## 🚀 Getting Started

Follow these steps to run the application locally on your machine.

### 1. Install Dependencies
Ensure you have Python 3 installed, then open your terminal and install the required libraries:
```bash
pip install eel pandas scikit-learn

```

### 2. Run the Application

Navigate to the root directory of the project and execute the main Python script:

```bash
python main.py

```

> *A new standalone window will open automatically, loading the celestial interface!*

## 📂 Project Structure

```text
📦 celestial-anime-recommender
 ┣ 📂 web/                  # Frontend assets
 ┃ ┣ 📜 index.html          # Main UI layout
 ┃ ┣ 📜 style.css           # Glassmorphism & animations
 ┃ ┗ 📜 script.js           # Live search & Eel bindings
 ┣ 📜 main.py               # Entry point & Eel server setup
 ┣ 📜 recommender.py        # TF-IDF algorithm & data processing logic
 ┗ 📜 anime.csv             # Anime dataset containing details & genres

```

---

## 🤝 Let's Connect






Made with 💖 and ☕ by Vaibhav Pandey
