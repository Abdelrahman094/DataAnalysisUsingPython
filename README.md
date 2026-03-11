<h1 align="center">Hi 👋, I'm Abdelrhman Muhammed</h1>
<h3 align="center">A passionate Data Analyst/Engineer</h3>

- 🔭 I’m currently working on <a href="https://github.com/Abdelrahman094/DataAnalysisUsingPython">Data Analysis Using Python on data retrieved from API</a>

- 🌱 I’m currently learning **Pandas, NumPy, and Exploratory Data Analysis (EDA)**

---

# 📊 DataAnalysisUsingPython

This project demonstrates **data analysis using Python on user data retrieved from an API**.  
The dataset is collected from the DummyJSON users API and analyzed using modern Python data analysis tools.

---

# 📌 Project Objectives

- Retrieve user data from an API
- Perform data exploration
- Clean and prepare the dataset
- Perform statistical analysis
- Visualize insights using Seaborn

---

# 🌐 Data Source

The dataset is retrieved from:
https://dummyjson.com/users?limit=100


The dataset contains fields such as:

- Age
- Gender
- Height
- Weight
- Eye Color
- Blood Group
- Address (City, Country)
- Role

---

# 📁 Project Structure

The dataset contains fields such as:

- Age
- Gender
- Height
- Weight
- Eye Color
- Blood Group
- Address (City, Country)
- Role

---

# 📁 Project Structure
DataAnalysisUsingPython
│
├── Proj
│ ├── read.py
│ ├── analysis.py
│ └── visualization.py
│
├── users.csv
└── README.md


---

# 📥 Data Collection

Data is fetched from the API using the Python `requests` library.

```
python
import requests
import pandas as pd

url = "https://dummyjson.com/users?limit=100"
response = requests.get(url)
data = response.json()['users']

df = pd.DataFrame(data)

🔎 Data Exploration

The project performs the following exploratory steps:

Dataset shape

Column names

Data types

Missing values detection

Duplicate row detection

Summary statistics

Value counts for categorical columns

🧹 Data Cleaning

Important fields such as city and country were extracted from the nested address column.

df['country'] = df['address'].apply(lambda x: x['country'])
df['city'] = df['address'].apply(lambda x: x['city'])

Missing values in age, height, and weight were handled using mean or median replacement when necessary.

📈 Analysis Performed

The analysis answers the following questions:

What is the average age of users?

What is the average age by gender?

How many users belong to each gender?

What are the top 10 cities with the most users?

What is the average height and weight of users?

Is there any relationship between age and height/weight?

📊 Data Visualization

Several visualizations were created using Seaborn, including:

Age distribution histogram

Users per gender count plot

Average age by gender bar plot

Age vs height scatter plot

Age vs weight scatter plot

Correlation heatmap

These visualizations help identify trends and relationships in the dataset.

🧠 Key Findings

The average user age is approximately mid-30s.

Gender distribution is relatively balanced.

Some cities contain higher numbers of users.

There is no strong relationship between age and height or weight based on correlation analysis.

Height and weight show a moderate relationship with each other.
