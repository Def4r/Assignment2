#This file is were the program runs and functions, here we create an object and simluate the 12 month report for the business

from Product import ProductClass
from time import sleep
import random

print("***Welcome to the Business Production Sim***")
print("")

Business = ProductClass()
Business.BusinessInfo()
Business.DisplayBusinessInfo()

print("")
sleep(1)
print("***Business in year statement***")
print("")

NetProfits = 0
Stock = Business.getStockLvl()
CurrentStock = Business.getStockLvl()

#Loops through each month generating and showing stock, sales and the current month 
for months in range(1, 13):
    sleep(2)
    sales = random.randint(-10 , 10)
    print("Month",months, ":")
    print("Manufactored: ",Business.getEstManufactored())
    print("Sold ",Business.salesEachMonth(sales))
    CurrentStock -= sales
    print("Stock Left:", CurrentStock)
    print("")
    MonthlyRev = (Business.salesEachMonth(sales) * Business.getProductPrice()) 
    MonthlyCost = (Business.salesEachMonth(sales) * Business.getManufactorCost()) 
    MonthlyProfits = MonthlyRev - MonthlyCost
    NetProfits += MonthlyProfits

#Shows the Netprofits after 12 months has passed
print("Net Profits over 12 Months : $", NetProfits)




