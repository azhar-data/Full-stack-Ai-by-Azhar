# Full Stack AI by Azhar

A hands-on learning repository documenting my journey from Python fundamentals to data analysis, machine learning, deep learning, web scraping, and Generative AI. It contains Python scripts, practice exercises, and datasets organized by learning week/topic.

> **Purpose:** learning, experimentation, and building practical skills across the data and AI workflow.

## Repository at a Glance

| Area | What's included |
|---|---|
| Python fundamentals | Arithmetic, strings, data types, lists, tuples, sets, dictionaries, comparison/logical operators, conditions, loops, and control-flow statements |
| NumPy | Array-based practice and numerical exploration using property and startup-investment datasets |
| Pandas | Loading and exploring tabular data, data manipulation, and analysis with real-estate and startup datasets |
| Data visualization | Seaborn exercises using property and real-estate data |
| Web scraping | Practice scripts using BeautifulSoup and Selenium, including example product/website scraping |
| Machine learning practice | Example workflows for customer churn, diamond prices, housing data, loan prediction, and smartphone data |
| Deep learning | Fashion-MNIST classification practice |
| Generative AI | An introductory GenAI script and related experiments |
| Datasets | CSV files for real estate, Zameen property listings, startup investments, telecom churn, diamonds, housing, loans, and smartphones |

## Folder Guide

### `Week 1/` — Python Basics
Core syntax and programming concepts:
- Arithmetic and string operations
- Data types and collections: lists, tuples, sets, and dictionaries
- Conditional statements and comparison/logical operators
- Loops, `break`, `pass`, and `continue`

### `Week 2/Numpy/` — NumPy Practice
- Numerical operations with NumPy
- Property-data and startup-investment exercises
- Related CSV datasets

### `Week 2/Pandas/` — Data Analysis
- Pandas practice with real-estate and startup-investment datasets
- CSV loading and tabular data exploration

### `Week 4/` — Visualization
- Seaborn practice
- Visual exploration of Zameen property listings and US real-estate data

### `Week 6/` — Web Scraping
- BeautifulSoup examples
- Selenium examples for website and product-page scraping

### `Week 8/` — Machine Learning and Tabular Datasets
Practice scripts and datasets covering:
- Telecom customer churn
- Diamond data and price-related analysis
- Housing data
- Loan prediction
- Smartphone data

These files are learning examples; results and model quality depend on preprocessing, validation, and the dataset used.

### `week 10/` — Deep Learning and Generative AI
- Fashion-MNIST deep-learning practice
- Introductory Generative AI code
- Supporting Python scripts

## Tech Stack

- **Language:** Python
- **Data work:** NumPy, Pandas
- **Visualization:** Seaborn
- **Web scraping:** BeautifulSoup, Selenium
- **Machine learning / deep learning:** example scripts and datasets for model-building practice
- **Data formats:** CSV

The exact third-party packages vary by script. Install the libraries required by the particular file you want to run.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/azhar-data/Full-stack-Ai-by-Azhar.git
cd Full-stack-Ai-by-Azhar
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install the libraries needed for your chosen script

For example, data-analysis and visualization exercises may use:

```bash
python -m pip install numpy pandas matplotlib seaborn
```

Scraping scripts may additionally require:

```bash
python -m pip install beautifulsoup4 selenium requests
```

Machine-learning and deep-learning scripts may need other packages. Check the imports at the top of each file and install the relevant dependencies before running it. Selenium may also require a compatible browser/driver setup.

### 4. Run a Python file

Paths containing spaces should be quoted. For example:

```bash
python "Week 1/Arthmetic_opreation.py"
```

Choose a script and dataset from the same topic folder. Some scripts expect a CSV path or environment that may need adjusting on your computer.

## Working with the Datasets

- Keep each dataset paired with the exercise that uses it.
- Check column names and file paths before running a script.
- Inspect missing values, duplicates, data types, and target-column definitions before training a model.
- Use appropriate train/test splits and evaluation metrics for machine-learning experiments.
- Follow the source dataset's licence and terms when reusing or redistributing data.

## Notes

- This repository is a growing collection of learning exercises and experiments, not one single deployable full-stack application.
- Folder names reflect the current learning-week organization; the numbering may skip weeks.
- File names and scripts may be refined as the projects evolve.
- No performance scores or production-readiness claims are made by this README.

## About Me

**Muhammad Azhar** — learning and building in Python, data analysis, machine learning, deep learning, and Generative AI.

- GitHub: https://github.com/azhar-data
- LinkedIn: https://www.linkedin.com/in/muhammad-azhar-ai-engineer

---

If you find the repository useful, feel free to ⭐ star it or share suggestions for improvement.
