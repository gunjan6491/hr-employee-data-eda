import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load and inspect the dataset
df=pd.read_csv("data_analytics_projects/Employee.csv")
print(df.head(5))
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().value_counts())
print(df.describe())

# cleaning the data
df=df.drop_duplicates()
print(df.duplicated().sum())

df["Department"]=df["Department"].str.capitalize()

print(df["Department"])

df["LeftCompany"]=df["LeftCompany"].str.capitalize()

s=np.array(df["Salary"])
tru=np.isnan(s)
s[tru]=df["Salary"].mean()
df["Salary"]= s
print(df.isnull().sum())

zer=np.array(df["PerformanceScore"])
tru=np.isnan(zer)
zer[tru]= 1

def category(x):
    if x<4:
        return "junior"
    elif x>=4 and x<=8:
        return "mid"
    else:
        return "senior"
    

df["positon"]=df["Experience (Years)"].apply(category)
print(df.head())


# analysis
print(df.describe())
print(df["EmployeeID"].value_counts().sum())
print(df.columns)

left=df[df["LeftCompany"]=='Yes']
print(left.value_counts().sum())

avg=df.groupby("Department")["Salary"].mean()
print(avg)

emp=df.groupby("Department")["EmployeeID"].count()
print(emp)

left=df[df["LeftCompany"]=="Yes"].groupby("Department")["EmployeeID"].count()
print(left)

avr=df.groupby("Department")["Experience (Years)"].mean()
print(avr)

avr=df.groupby("Department")["PerformanceScore"].mean()
print(avr)

#insights
jun=df[df["LeftCompany"]=="Yes"].groupby("positon")["LeftCompany"].count()
print(jun)

yes=df[df["LeftCompany"]=="Yes"].groupby("LeftCompany")["PerformanceScore"].mean()
print(yes)

no=df[df["LeftCompany"]=="No"].groupby("LeftCompany")["PerformanceScore"].mean()
print(no)

core=df[['Experience (Years)',"Salary"]].corr()
print(core)

#visualize

plt.hist(df["Salary"],bins=10)
plt.xlabel("salary range")
plt.ylabel("number of employee")
plt.title(" common salary ranges")
plt.show()

left=df[df["LeftCompany"]=="Yes"].groupby("Department")["EmployeeID"].count()
plt.bar(left.index,left.values)
plt.xlabel("departments-->")
plt.ylabel("no. of employees left")
plt.title(" employee left from each department")
plt.show()

jun=df.groupby("positon")["EmployeeID"].count()
plt.bar(jun.index,jun.values)
plt.xlabel("seniority level-->")
plt.ylabel("number of employes-->")
plt.title("employee counts in each SeniorityLevel")
plt.show()

plt.scatter(df["Experience (Years)"],df["Salary"],marker='*')
plt.xlabel("years of experience")
plt.ylabel("salary-->")
plt.title("relation between experience and salary")
plt.show()

avg=df.groupby("Department")["Salary"].mean()
plt.bar(avg.index,avg.values)
plt.xlabel("department-->")
plt.ylabel("salary-->")
plt.title("salary per department")
plt.show()