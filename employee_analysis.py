import pandas as pd
import matplotlib.pyplot as plt

# Sample employee dataset
data = {
    "EmployeeID": range(1, 101),
    "Department": [
        "HR" if i % 5 == 0 else
        "Finance" if i % 5 == 1 else
        "Engineering" if i % 5 == 2 else
        "Sales" if i % 5 == 3 else
        "Marketing"
        for i in range(1, 101)
    ],
    "Region": ["North", "South", "East", "West"] * 25
}

df = pd.DataFrame(data)

# ✅ Calculate frequency count for HR
hr_count = (df["Department"] == "HR").sum()
print("Frequency count for HR department:", hr_count)  # Console output

# ✅ Create histogram
plt.figure(figsize=(6,4))
df["Department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("chart.png")

# ✅ Save HTML report with HR count INCLUDED
with open("employee_report.html", "w") as f:
    f.write(f"""
    <html>
    <head><title>Employee Performance Analysis</title></head>
    <body>
        <h2>Employee Performance Analysis</h2>
        <p>Email: 23f1000504@ds.study.iitm.ac.in</p>
        <p><b>Frequency count for HR department: {hr_count}</b></p>
        <img src="chart.png" alt="Histogram" width="500">
    </body>
    </html>
    """)
