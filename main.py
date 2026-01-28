# PYTHON WORKFLOW

#1. Data Collection
import pandas as pd

df = pd.read_csv("blinkit_data.csv")
print(df.head())
print(df.info())

---------------------------------------------------------
#2. Data Cleaning
## Remove duplicates
df.drop_duplicates(inplace=True)

## Handle missing values
df.dropna(inplace=True)

## Standardize Fat Content
df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({
    'LF':'Low Fat',
    'Low Fat':'Low Fat',
    'reg':'Regular'
})

-----------------------------------------------------------
#3. Data Preprocessing
import numpy as np

## Convert year to int
df['Outlet_Establishment_Year'] = df['Outlet_Establishment_Year'].astype(int)

## Revenue column
df['Revenue'] = df['Sales']

## Sales millions
total_sales = np.round(df['Revenue'].sum()/1_000_000,2)

----------------------------------------------------------------
#4. Analysis
## KPIs
avg_sales = df['Sales'].mean()
avg_rating = df['Rating'].mean()
no_items = df.shape[0]

## Fat content analysis
fat_analysis = df.groupby('Item_Fat_Content').agg(
    Total_Sales=('Sales','sum'),
    Avg_Sales=('Sales','mean'),
    Items=('Sales','count'),
    Avg_Rating=('Rating','mean')
)

## Outlet size contribution
outlet_size = df.groupby('Outlet_Size')['Sales'].sum()

--------------------------------------------------------------------
#5. Export Clean Data
df.to_csv("clean_blinkit.csv", index=False)

----------------------------------------------
# SQL ANALYSIS
## KPIs
SELECT SUM(Sales), AVG(Sales), COUNT(*), AVG(Rating) FROM BlinkIT;
## Fat Content
SELECT Item_Fat_Content, SUM(Sales), AVG(Sales), COUNT(*)
FROM BlinkIT GROUP BY Item_Fat_Content;
## Outlet Location
SELECT Outlet_Location_Type, SUM(Sales)
FROM BlinkIT GROUP BY Outlet_Location_Type;
## Outlet Type
SELECT Outlet_Type, SUM(Sales), AVG(Sales)
FROM BlinkIT GROUP BY Outlet_Type;

-------------------------------------------------------------------------

# DAX CALCULATIONS:
Total Sales = SUM(BlinkIT[Sales])

Avg Sales = AVERAGE(BlinkIT[Sales])

No of Items = COUNTROWS(BlinkIT)

Avg Rating = AVERAGE(BlinkIT[Rating])

Sales % = DIVIDE(
    SUM(BlinkIT[Sales]),
    CALCULATE(SUM(BlinkIT[Sales]), ALL(BlinkIT))
)
