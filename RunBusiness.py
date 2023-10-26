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

print("Net Profits over 12 Months : $", NetProfits)




