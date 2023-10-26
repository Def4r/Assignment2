from Product import ProductClass
from time import sleep
import random

print("***Welcome to the Business Production Sim***")
print("")

Business = ProductClass()
Business.BusinessInfo()
Business.DisplayBusinessInfo()

NetProfits = 0
Stock = Business.getStockLvl()
for months in range(1, 13):
    sleep(2)
    sales = random.randint(-10 , 10)
    print("Month",months, ":")
    print("Manufactored: ",Business.getEstManufactored())
    print("Sold ",Business.salesEachMonth(sales))
    print("Stock Left:", Business.remainingStock(sales, Stock))
    print("")
    MonthlyProfits = (Business.salesEachMonth(sales) * Business.getProductPrice()) - Business.getManufactorCost()
    NetProfits += MonthlyProfits
    
print("Net Profits over 12 Months : $", NetProfits)




