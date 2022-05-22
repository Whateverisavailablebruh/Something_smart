import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


N= input("Enter the stock code ")
N1= input("Enter the stock code ")
T= input("Enter the time frame ")

stock = yf.Ticker(N)
stck=stock.history(period=T)
stck.reset_index(inplace=True)
s= list(stck['Open'])
d= list(stck['Date'])

stock1 = yf.Ticker(N1)
stck1=stock1.history(period=T)
stck1.reset_index(inplace=True)
s1= list(stck1['Open'])
d1= list(stck1['Date'])

plt.style.use("seaborn-pastel")
plt.plot(d,s)
plt.plot(d1,s1)
plt.title(N+" vs "+N1+" Stock price "+T)
plt.ylabel("Stock price")
plt.xlabel("Date")
plt.legend([N,N1])
plt.tight_layout()
plt.show()