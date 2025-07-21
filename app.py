import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Read the data
df = pd.read_csv("student_marks.csv")
# Step 2: Basic info
print("All Student Marks:\n")
print(df)
# Step 3: Calculate total and average marks
df["Total"] = df[["Math", "Physics", "Chemistry", "English", "CS"]].sum(axis=1)
df["Average"] = df["Total"] / 5
# Step 4: Find the Topper
topper = df.loc[df["Total"].idxmax()]
print("\n Topper:\n", topper["Name"])
print("Total Marks:", topper["Total"])
# Step 5: Subject-wise average
subject_avg = df[["Math", "Physics", "Chemistry", "English", "CS"]].mean()
print("\n Subject-wise Average Marks:\n", subject_avg)
# Step 6: Visualize average marks per student
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Average"], color='skyblue')
plt.title(" Average Marks of Each Student")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
# Step 7: Visualize subject-wise average
plt.figure(figsize=(10, 5))
plt.bar(df['Name'], df['Total'])
plt.title(" Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
