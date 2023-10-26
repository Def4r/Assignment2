from Product import ProductClass
from time import sleep

print("***Welcome to the Business Production Sim***")

Business = ProductClass()
Business.BusinessInfo()
Business.DisplayBusinessInfo()

for months in range(1, 13):
    sleep(1)
    print("Month",months, ":")
    print("Manufactored: ",Business.getEstManufactored())
    print("Sold ",Business.salesEachMonth())


