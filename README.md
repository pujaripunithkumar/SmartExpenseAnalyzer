# 💰 Smart Expense Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?style=for-the-badge&logo=flask&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge)

> *A lightweight, data-driven web application to track, analyze, and visualize personal finances.*

---

## 📖 Project Context
*Why this project?*
Financial literacy starts with awareness. I built the *Smart Expense Analyzer* to bridge the gap between complex finance apps and simple spreadsheets. This project demonstrates how *Python* can be used to build a full-stack solution that not only records data but provides actionable insights through visualization.

It solves the "black hole" spending problem by offering instant feedback on where money is going, without requiring a heavy database setup.

## ✨ Key Features
* *📉 Dynamic Visualization:* Automatically generates Matplotlib pie charts to visualize spending distribution.
* *⚡ Lightweight Architecture:* Uses a flat-file CSV system for data persistence, ensuring zero-latency reads/writes and easy portability.
* *📊 Smart Categorization:* Tags expenses (Food, Travel, Bills) for granular analysis.
* *💡 Budget Insights:* Provides logic-based feedback on spending habits.
* *📱 Responsive UI:* Clean HTML/CSS interface that works across devices.

## 🛠 Tech Stack
* *Backend:* Python, Flask
* *Data Processing:* Pandas (CSV manipulation, aggregation)
* *Visualization:* Matplotlib (Server-side image generation)
* *Frontend:* HTML5, CSS3, Jinja2 Templating
* *Deployment:* Replit

## 🚀 How to Run Locally
Instructions to set up the project on your local machine.

1.  *Clone the repository*
    bash
    git clone [https://github.com/yourusername/smart-expense-analyzer.git](https://github.com/yourusername/smart-expense-analyzer.git)
    cd smart-expense-analyzer
    

2.  *Install dependencies*
    bash
    pip install flask pandas matplotlib
    

3.  *Run the application*
    bash
    python app.py
    

4.  *Access the App*
    Open your browser and navigate to http://127.0.0.1:5000/

## 📂 Project Structure
```text
📦 Smart-Expense-Analyzer
 ┣ 📂 static
 ┃ ┣ 📜 style.css        # Custom styling
 ┃ ┗ 📜 chart.png        # Dynamically generated visualization
 ┣ 📂 templates
 ┃ ┣ 📜 index.html       # Dashboard UI
 ┃ ┗ 📜 add_expense.html # Data entry form
 ┣ 📜 app.py             # Main Flask application logic
 ┣ 📜 expenses.csv       # Data storage (Auto-generated)
 ┗ 📜 README.md          # Documentation
