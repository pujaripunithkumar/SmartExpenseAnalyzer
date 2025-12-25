# 💰 Smart Expense Analyzer

![Project Banner](static/banner.png)

[![Live Demo](https://img.shields.io/badge/Demo-Try%20it%20Live-success?style=for-the-badge&logo=replit)](https://code-pack--punithkumar72.replit.app)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?style=for-the-badge&logo=flask&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge)


> *A lightweight, data-driven web application to track, analyze, and visualize personal finances.*

---

## 📖 Project Context
*Why this project?*
Financial literacy starts with awareness. I built the *Smart Expense Analyzer* to bridge the gap between complex finance apps and simple spreadsheets. This project demonstrates how *Python* can be used to build a full-stack solution that not only records data but provides actionable insights through visualization and logic-based advice.

It solves the "black hole" spending problem by offering instant feedback on where money is going, without requiring a heavy database setup.

## ✨ Key Features
* *📉 Dynamic Visualization:* Automatically generates charts to visualize spending distribution.
* *⚡ Lightweight Architecture:* Uses a flat-file CSV system for data persistence, ensuring zero-latency reads/writes.
* *📊 Smart Categorization:* Tags expenses (Food, Travel, Bills) for granular analysis.
* *💡 Budget Advice:* A dedicated module that analyzes your data and offers financial tips.
* *📱 Responsive UI:* Clean HTML/CSS interface that works across devices.

## 🛠 Tech Stack
* *Backend:* Python, Flask
* *Data Processing:* Pandas (CSV manipulation, aggregation)
* *Visualization:* Matplotlib
* *Frontend:* HTML5, CSS3, Jinja2 Templating
* *Deployment:* Replit

## 🚀 How to Run Locally
Instructions to set up the project on your local machine.

1.  *Clone the repository*
    bash
    git clone [https://github.com/yourusername/SmartExpenseAnalyzer.git](https://github.com/yourusername/SmartExpenseAnalyzer.git)
    cd SmartExpenseAnalyzer
    

2.  *Install dependencies*
    bash
    pip install flask pandas matplotlib
    

3.  *Run the application*
    bash
    python main.py
    

4.  *Access the App*
    Open your browser and navigate to http://127.0.0.1:5000/

## 📂 Project Structure
```text
📦 SmartExpenseAnalyzer
 ┣ 📂 static
 ┃ ┗ 📜 style.css        # Custom styling
 ┣ 📂 templates
 ┃ ┣ 📜 index.html       # Dashboard / Home
 ┃ ┣ 📜 chart.html       # Visualization page
 ┃ ┣ 📜 summary.html     # Expense summary & Breakdown
 ┃ ┗ 📜 advice.html      # Logic-based budget tips
 ┣ 📜 main.py            # Main Flask application logic
 ┣ 📜 expenses.csv       # Data storage (Auto-generated)
 ┗ 📜 README.md          # Documentation
```
## 🔮 Future Roadmap
* [ ] *Database Migration:* Upgrade from CSV to SQLite/PostgreSQL for scalability.
* [ ] *User Auth:* Implement Login/Signup functionality.
* [ ] *Report Export:* Generate PDF monthly reports.
* [ ] *AI Insights:* Use basic ML to predict future expenses.

## 👨‍💻 Author
*Punith Kumar*
* Passionate about Python development and Data Analytics.
* [LinkedIn Profile](https://www.linkedin.com/in/punith-kumar-p-03673b326?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
* [GitHub Profile](https://github.com/pujaripunithkumar)
*

