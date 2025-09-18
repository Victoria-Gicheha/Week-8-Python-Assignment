## 📊 COVID-19 Research Publications Analysis
## 📝 Assignment

In this assignment, you will analyze the CORD-19 (COVID-19 Open Research Dataset) to explore research publication patterns. You will work with both Jupyter Notebooks and a Streamlit app to demonstrate the complete data science workflow — from loading data, cleaning, analysis, visualization, and building an interactive dashboard.

## 🎯 Learning Objectives

By completing this assignment, you will:

Practice loading and exploring real-world datasets.

Apply Python data analysis libraries (pandas, numpy, matplotlib, seaborn).

Generate meaningful visualizations (bar charts, word clouds, top categories).

Build and deploy a simple Streamlit application to share insights interactively.

Understand how to structure a data science project with clear deliverables.

Learn to manage dependencies using a virtual environment and requirements.txt.

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
Make sure you are using Python 3.7+.
Installed Packages: Matplotlib, numpy, pandas, streamlit, seaborn, Jupyter Notebook
Install dependencies inside a virtual environment:
GitHub Repo.

# Create and activate venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # On PowerShell

# Install requirements
pip install -r requirements.txt

Contents of requirements.txt:
pandas
numpy
matplotlib
seaborn
wordcloud
streamlit
jupyter

## ▶️ Running the Project
1. Run the Jupyter Notebook
Open the notebook and run cells step by step:
jupyter notebook cord19_exploration.ipynb

2. Run the Streamlit App
Launch the interactive dashboard:
streamlit run app.py


Then open the local URL (default: http://localhost:8501
) in your browser.

## 📊 Visualizations
The analysis includes:
📅 Publications per year (bar chart)
📚 Top journals by publications (horizontal bar chart)
🔤 Word frequency of research titles
☁️ Word cloud visualization of title keywords

These appear both in the notebook and in the Streamlit app.

## ✅ Expected Outcomes
By completing this project, you will have:

A Jupyter Notebook (cord19_exploration.ipynb) with your analysis.
Several visualizations showing research patterns.
A Streamlit app (app.py) displaying findings interactively.
A requirements.txt file to reproduce your environment.
Basic hands-on experience with the data science workflow.

## 📤 Submission Instructions

Submit a zipped project folder containing:
app.py
cord19_exploration.ipynb
requirements.txt
README.md

## ▶️Link to the dataset used.
Pick the metadata csv - (https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

## 📦Installation
1. Clone this repo
2. Navigate to the project folder
3. Create & activate a virtual environment
4. Run:
   pip install -r requirements.txt

