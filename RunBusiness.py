from Product import ProductClass
from time import sleep
import random

print("***Welcome to the Business Production Sim***")

Business = ProductClass()
Business.BusinessInfo()
Business.DisplayBusinessInfo()

for months in range(1, 13):
    sleep(2)
    sales = random.randint(-10 , 10)
    print("Month",months, ":")
    print("Manufactored: ",Business.getEstManufactored())
    print("Sold ",Business.salesEachMonth(sales))
    print("Stock Left:", Business.remainingStock(sales))
    print("")


