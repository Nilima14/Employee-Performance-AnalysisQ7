import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "EmployeeID": range(1, 21),
    "Department": ["HR", "IT", "Finance", "Sales", "Marketing"] * 4,
    "PerformanceScore": [85, 78, 92, 88, 76, 90, 81, 87, 95, 83,
                         77, 89, 91, 84, 80, 86, 93, 82, 79, 88],
    "Region": ["North", "South", "East", "West"] * 5
}

df = pd.DataFrame(data)

# ✅ Frequency count for HR department
hr_count = (df["Department"] == "HR").sum()
print("Frequency count for HR department:", hr_count)

# ✅ Create histogram
plt.figure(figsize=(6, 4))
df["Department"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()

# Save chart as HTML
html_file = "employee_report.html"
with open(html_file, "w") as f:
    f.write("<html><head><title>Employee Report</title></head><body>\n")
    f.write("<h2>Employee Department Distribution</h2>\n")
    f.write(f"<p>Email: 23f1000504@ds.study.iitm.ac.in</p>\n")
    f.write(f"<p>Frequency count for HR department: {hr_count}</p>\n")
    # Save PNG and embed
    plt.savefig("chart.png")
    f.write('<img src="chart.png" width="600">\n')
    f.write("</body></html>")

print(f"Report saved as {html_file}")
