## 📊 CORD-19 Data Exploration & Streamlit App
## 📝 Assignment

This project explores the CORD-19 metadata dataset through a complete data science workflow. The tasks include:
1. Loading and exploring the dataset.
2. Cleaning and preparing the data.
3. Performing basic analysis and creating visualizations.
4. Building a simple Streamlit application to display findings.
5. Documenting the process, reporting insights, and reflecting on challenges.

## 🎯 Learning Objectives

By completing this project, you will:
~ Learn how to load, explore, and clean real-world datasets.
~ Practice creating new features and preparing data for analysis.
~ Gain experience with data visualization using Matplotlib and WordCloud.
~ Build an interactive Streamlit app for data exploration.
~ Document findings and reflect on challenges faced in the workflow.

## 📂 Project Structure
WEEK-8/
│── app.py                   # Streamlit app
│── cord19_exploration.ipynb # Jupyter notebook with analysis
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation (this file)
│── data/                    # Folder for dataset(s)
│   └── cord19.csv           # COVID-19 publications dataset
│── .venv/                   # Virtual environment (not included in submission)

## 📦 Requirements
* Python 3.7+.
* Installed Packages: Matplotlib, numpy, pandas, streamlit, seaborn, Jupyter Notebook
* Install dependencies inside a virtual environment:
* GitHub Repo.


## 🚀 Deliverables

* cord19_exploration.ipynb → Jupyter Notebook with step-by-step analysis.
* app.py → Streamlit app to interactively explore findings.
* requirements.txt → List of dependencies for reproducibility.
* README.md → Documentation of the project, findings, and reflection.

# Create and activate venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # On PowerShell

## ▶️ Running the Project
1. Run the Jupyter Notebook
Open the notebook and run cells step by step:
jupyter notebook cord19_exploration.ipynb

2. Run the Streamlit App
Launch the interactive dashboard:
streamlit run app.py

Then open the local URL (default: http://localhost:8501
) in your browser.

## 📊 Expected Outcomes

#By completing this assignment, you will have:
#A Jupyter notebook or Python script with your analysis.
#Several visualizations showing patterns in the data.
#A simple Streamlit app that displays the findings.
#Hands-on experience with the data science workflow.

## 🛠️ Installation
1. Clone this repository or download the project folder.
2. Navigate to the project directory:
3. Create and activate a virtual environment: [python -m venv .venv
.venv\Scripts\Activate.ps1   # for PowerShell]
4. Install dependencies: [pip install -r requirements.txt]
5. Run the Streamlit app: [streamlit run app.py]

## 📈 Analysis & Visualizations

* Publications per Year → Bar chart showing number of papers published each year.
* Top Journals → Horizontal bar chart of journals with the highest number of papers.
* Word Frequency → Most common words in paper titles.
* Word Cloud → Visualization of common words in titles.

## 🔍 Findings

* Research activity peaked in 2020, reflecting the urgency of COVID-19 studies.
* Preprint servers such as medRxiv and bioRxiv contributed a large share of publications.
* Frequent words in titles included covid-19, coronavirus, sars-cov-2, pandemic.
* Abstract word counts varied widely, reflecting different publication formats (brief notes vs. full research articles).

## 💭 Reflection

* Learned how to clean and preprocess large datasets, including handling missing values and converting dates.
* Understood the value of feature engineering (e.g., abstract word count) for deeper insights.
* Faced challenges with the large dataset size (performance issues, loading times).
* Gained experience building an interactive Streamlit app for presenting results.
* Practiced Git/GitHub best practices, including using .gitignore for large datasets and maintaining requirements.txt for reproducibility.

## 📤 Submission Instructions

Submit project folder containing:
1. app.py
2. cord19_exploration.ipynb
3. requirements.txt
4.README.md

## ▶️Link to the dataset used.
Pick the metadata csv - (https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

