# hr-employee-data-eda
Exploratory data analysis and visualization of HR employee attrition, salary trends, and performance metrics using pandas and matplotlib

# HR Employee Attrition Analysis 📊

This project analyzes HR employee data to uncover trends in attrition, salary distribution, performance, and experience levels. The entire analysis is done using plain Python scripts — no Jupyter Notebook involved.

---

## 🔍 Objective

To clean, analyze, and visualize HR employee data using core data analytics techniques and Python libraries. Key questions explored:

- Which departments have higher attrition?
- Are Juniors more likely to leave than Seniors?
- How does experience impact salary?
- Is performance linked to attrition?

---

## 🛠️ Tools Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## ✅ Key Steps

### 1. Data Cleaning
- Removed duplicates
- Standardized column values
- Handled missing values
- Cleaned and categorized `Department` and `LeftCompany`

### 2. Feature Engineering
- Created a new column: `positon` (Junior, Mid, Senior) based on experience level

### 3. Data Analysis
- Department-wise attrition
- Average salary by department
- Performance score vs attrition
- Experience vs salary correlation

### 4. Data Visualization
- Salary distribution (histogram)
- Employees left by department (bar chart)
- Employee count by position (bar chart)
- Salary vs experience (scatter plot)
- Average salary per department (bar chart)

---

## 📊 Sample Insights

- Juniors had the highest attrition rate overall.
- Sales and Finance departments saw the most turnover.
- Experience showed a positive (but not perfect) correlation with salary.
- Employees who left had slightly lower average performance scores.

---

## 🏁 Conclusion

This project demonstrates end-to-end real-world HR data analytics using only Python scripts — from raw data to business insights and clear, compelling visualizations.


## ⭐ Star the repository if you found this helpful!
