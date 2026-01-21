# 📰 DailyBrieflyAI
**An intelligent system for curated daily news summaries**

DailyBrieflyAI is an intelligent system designed to curate and summarize the day's most important news by category. Instead of overwhelming the user with endless feeds, the system selects and presents the top 10 most current, significant, and impactful articles based on the user's selection. 

Leveraging the **Google Gemini API**, the system filters out the noise and delivers high-value insights in a clean, professional, and readable format.

---

<<div align="center">
  <h2>✨ Application Demo</h2>
  <img src="./assets/demo.gif" 
       alt="Application Demo" 
       style="max-width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
</div>

---

### 🚀 How it works
The application scans pre-defined RSS sources, automatically filtering out sponsored content and outdated news. **Google Gemini** then analyzes the headlines to select the top 10 most impactful stories. Finally, the system scrapes the full article content, removes web noise (ads/scripts), and the AI generates a concise, summary presented in a high-end **Gradio** interface.

### ✨ Key Features
* **Smart AI Curation:** Combines programmatic filtering with AI reasoning to ensure relevance, eliminate duplicates, and summarize the relevant data.
* **Modern UI:** A clean and responsive interface designed for a reading experience.
---

### 🛠️ Tech Stack
* **AI:** Google Gemini API
* **UI:** Gradio
* **Environment:** Python 3.x

---

### 📁 Project Structure
* `DailyBrieflyAI.ipynb`: Main dashboard and UI for generating the daily briefing
* `scraping.py`: Contains the logic for news harvesting, HTML cleaning, and CSS styling.
* `prompts.py`: Houses the sophisticated System and User prompts that guide the AI's reasoning.
* `requirements.txt`: A list of all necessary Python dependencies.

---
## 🏁 Getting Started

### 1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

### 2. **Environment Variables:** 
Create a .env file in the root directory with the following Variables

| Variable | Purpose |
| :--- | :--- |
| `GEMINI_API_KEY` | Your Google Gemini API Key |
| `MODEL` | Your preferred model |

### 3. **Run the Application:** 
Open the Jupyter Notebook (DailyBrieflyAI.ipynb) and execute the cells. The Gradio interface will launch, allowing you to select a category and build your daily edition.

---

📞 Contact with me: 
**Orit Alster** - [LinkedIn Profile](https://www.linkedin.com/in/orit-davidyan-alster-61aa2b144)

