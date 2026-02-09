# Amazon Sales Data Visualization using Matplotlib

## Project Overview
This project analyzes and visualizes Amazon sales data using Python and Matplotlib.  
The objective is to understand sales trends, category performance, and revenue distribution through graphical representation.

## Objectives
- Read Amazon sales data from a CSV file
- Clean and preprocess the data
- Visualize sales trends using Matplotlib
- Extract useful insights from the visualizations

## Technologies Used
- Python 3
- Pandas
- Matplotlib
- VS Code

## Dataset
The dataset is a CSV file containing Amazon sales data.

Example columns:
- Order Date
- Product Category
- Sales
- Profit
- Quantity

Dataset source: Kaggle or any public Amazon sales dataset.

## Visualizations
- Sales over time (Line Chart)
- Category-wise sales (Bar Chart)
- Profit distribution (Histogram)
- Sales contribution by category (Pie Chart)

## How to Run the Project

1. Clone the repository:
   git clone https://github.com/Abhi-ops-hub/Amazon-Sales-Visualisation-using-matplotlib.git

2. Install required libraries:
   pip install pandas, matplotlib

3. Run the Python file:
   code.py

## Sample Code
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_sales.csv")

plt.plot(df["Order Date"], df["Sales"])
plt.title("Amazon Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

## Results and Insights
- Identified peak sales periods
- Analyzed best performing product categories
- Observed overall sales trends

## Future Enhancements
- Add advanced visualizations
- Create an interactive dashboard
- Apply machine learning for sales prediction

## Author
Abhishek Goswami
Email: abhishekgoswamipvt@gmail.com

