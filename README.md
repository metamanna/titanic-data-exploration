# titanic-data-exploration
Exploratory Data Analysis of the Titanic dataset using Python. Includes data cleaning, feature engineering, and custom visualizations to uncover survival patterns based on class, age, title, and family size. Built with pandas, seaborn, matplotlib, and NumPy.

# Titanic Data Exploration

A comprehensive and aesthetic deep-dive into the Titanic dataset—this notebook walks through cleaning, feature engineering, and storytelling-driven visualizations to uncover what influenced passenger survival.

---

## Project Structure

- `Titanic-Dataset.csv` → Original dataset
- `titanic_analysis.ipynb` → Main notebook for data cleaning, EDA & visuals
- `README.md` → Project overview

---

## Technologies Used

- Python 3.x  
- pandas, NumPy  
- seaborn, matplotlib  
- Jupyter Notebook

---

## Key Steps

1. **Data Cleaning**  
   - Handled empty strings and missing values  
   - Dropped sparse columns like `Cabin`

2. **Feature Engineering**  
   - Extracted `Title` from passenger names  
   - Created `FamilySize` feature from `SibSp` + `Parch`

3. **Visual Storytelling**  
   - Violin plots, donut charts, facet grids  
   - Explored survival by class, age, title & family size

---

## Goal

To build an interactive, clean, and visually appealing narrative around Titanic passenger survival—bridging storytelling with data science.

---

## Sample Visual

![survival-pie-chart](path/to/your/image.png)  
*(Optional: include a screenshot or demo GIF here)*

---

## Dataset

- [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)

---

## Author

Tamanna · *Data Explorer & Feature Artist*  
Crafted using insights, aesthetics, and Python 
