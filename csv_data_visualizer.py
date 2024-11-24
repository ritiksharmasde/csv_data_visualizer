import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = "output.csv"  
try:
    data = pd.read_csv(file_path)
    print("Data Loaded Successfully")
    print(data.head())  
except Exception as e:
    print(f"Error loading file: {e}")
    exit()


column_name = "Med. Age"
if column_name in data.columns:
    try:
        
        data[column_name] = pd.to_numeric(data[column_name], errors='coerce')  
        print(f"Column '{column_name}' successfully converted to numeric!")
    except ValueError as e:
        print(f"Error converting column '{column_name}': {e}")
else:
    print(f"Column '{column_name}' not found in the dataset!")

# -----------------------------------------------------------


column_name = "Med. Age"  
if column_name not in data.columns:
    print(f"Column '{column_name}' not found in dataset!")
    exit()


data[column_name] = pd.to_numeric(data[column_name], errors='coerce')  
values = data[column_name].dropna() 

mean = np.mean(values)
median = np.median(values)

mode = values.mode()[0] if not values.mode().empty else None  
variance = np.var(values)
std_deviation = np.std(values)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"variance: {variance}")
print(f"standard deviation: {std_deviation}")

# -----------------------------------------------------------


plt.figure(figsize=(10, 5))
plt.bar(data['Country (or dependency)'], data['Med. Age'].astype(float))  
plt.title('Net Change by Country')
plt.xlabel('Country')
plt.ylabel('Net Change')
plt.xticks(rotation=90)  
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.hist(values, bins=20, edgecolor='black', alpha=0.7)
plt.title('Distribution of Net Change')
plt.xlabel('Net Change')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 6))
plt.bar(['Mean', 'Median', 'Mode', 'Variance', 'Standard Deviation'], [mean, median, mode if mode is not None else 0,variance, std_deviation], color=['blue', 'green', 'red','purple', 'orange'])
plt.title('Mean, Median, Variance, Standard and Deviation')
plt.ylabel('Values')
plt.show()