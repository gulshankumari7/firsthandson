import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as num
url='/content/MVR.csv'
df=pd.read_csv(url)
print(df)

#Measure of central tendency of Open_M 
mean_value=df['Open_M'].mean()
print(f"mean value:-{mean_value}")
median_value=df['Open_M'].median()
print(f"median value:-{median_value}")
mode_value=df['Open_M'].mode()
print(f"mode value:-{mode_value}")

#Measure of volatility of Open_M 
var_value=df['Open_M'].var()
print(f"variable value:-{var_value}")
std_value=df['Open_M'].std()
print(f"standard deviation value:-{std_value}")

#Measure of central tendency of Close_M 
mean_value=df['Close_M'].mean()
print(f"mean value:-{mean_value}")
median_value=df['Close_M'].median()
print(f"median value:-{median_value}")
mode_value=df['Close_M'].mode()
print(f"mode value:-{mode_value}")

#Measure of volatility of Close_M 
var_value=df['Close_M'].var()
print(f"variable value:-{var_value}")
std_value=df['Close_M'].std()
print(f"standard deviation value:-{std_value}")

#Histogram plot of Open_M
plt.hist(df['Open_M'],bins=30,color="blue",edgecolor='black')
plt.title('Distribution of open market price')
plt.xlabel('Open_M')
plt.ylabel('Count')
plt.show()

#Histogram plot of Close_M
plt.hist(df['Close_M'],bins=30,color="blue",edgecolor='black')
plt.title('Distribution of close market price')
plt.xlabel('Close_M')
plt.ylabel('Count')
plt.show()
