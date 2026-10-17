import numpy as np
import pandas as pd
from openpyxl.workbook import Workbook

#loading the dataset
df = pd.read_csv('sample_employees.csv')
pd.set_option('display.max_columns', None)
print("Head: ", df.head())
print("Shape: ", df.shape)
print("Info: ", df.info())
print("Describe: ", df.describe())

#checking missing values
print("Missing values in each column")
print(df.isnull().sum())

#age-2, salary-1, performance_score-2
df['age'] = df['age'].fillna(df['age'].median())
df['salary'] = df['salary'].fillna(df['salary'].mean())
df['performance_score'] = df['performance_score'].fillna(df['performance_score'].median())

#replacing inf values
# df.replace([np.inf, -np.inf], np.nan, inplace=True)
# df.fillna(df.mean(), inplace=True)

#removing duplicates
print(df.duplicated())
df.drop_duplicates(inplace=True)

#converting join data to date-time format
df['join_date'] = pd.to_datetime(df['join_date'])
df["join_year"] = df["join_date"].dt.year
print(df.info())


#filtering with some condition
engineer_salary = df[(df['department'] == 'Engineering') & (df['salary'] > 70000)]
emp_delhi = df[(df['city'] == 'Delhi') & (df['performance_score'] > 4)]
print("Engineer salary more than 70000")
print(engineer_salary)
print("Employee from delhi with performance score more than 4")
print(emp_delhi)

#grouping 
print("Average salary per department")
avg_salary_per_dept = df.groupby("department")["salary"].mean()
print(avg_salary_per_dept)

print("Employee count per city")
emp_count_per_city = df.groupby("city")["employee_id"].count()
print(emp_count_per_city)

#sorting 
print("Top 5 highest paid employee")
highest_paid = df.sort_values("salary", ascending=False).head(5)
print(highest_paid)

#creating new column for salary per year experience
df["salary_per_year_exp"] = np.where(
    df["experience_years"] == 0,
    df["salary"],                              # if 0 years, just use salary
    df["salary"] / df["experience_years"]      # otherwise divide
)

#saving the file
df.to_excel('cleaned_sample_employees.xlsx', index=False)
print("Data cleaned successfully, file saved!")

