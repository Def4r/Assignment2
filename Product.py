#This is the product class. This is were all of the class were we initialze all of the business information needed to run the code 

import random
from UserChecking import userVI
from UserChecking import userVII
from UserChecking import userVIII

class ProductClass:
    
    def __init__(self, productName = "", productCode = 0, productSalesPrice = 0, manufactorCost = 0, stockLevel = 0, estManufactoredMnthly = 0):
        self.__productName = productName
        self.__productCode = productCode
        self.__productSalesPrice = productSalesPrice
        self.__manufactorCost = manufactorCost
        self.__stockLevel = stockLevel
        self.__estManufactoredMnthly = estManufactoredMnthly
    
    #returns estimated manufacture amount of products each month
    def getEstManufactored(self):
        return self.__estManufactoredMnthly
    
    #returns the stock level for the product 
    def getStockLvl(self):
        return self.__stockLevel

    #returns the price for the product 
    def getProductPrice(self):
        return self.__productSalesPrice

    #returns the manufacture cost
    def getManufactorCost(self):
        return self.__manufactorCost

    #asks the user for the business info needed to run the program 
    def BusinessInfo(self):
        self.__productName = input("Whats is the name of your product? :")
        self.__productCode = userVI("What is the code for your product? :", 100, 1000)
        self.__productSalesPrice = userVII("How much would you price your products? CAD ONLY $", 0)
        self.__manufactorCost = userVII("How much does it cost to make your product? CAD ONLY $", 0)
        self.__stockLevel = userVII("How much do you currently have in your stock? :", 0)
        self.__estManufactoredMnthly = userVIII("How much do you manufacture every month. This is an Estimate. :", 0)

    #Shows the user the business info they had just inputed
    def DisplayBusinessInfo(self):
        print("")
        print("Product Name:", self.__productName)
        print("Product Code:", self.__productCode)
        print("")
        print("Product Price:","$", self.__productSalesPrice, "CAD")
        print("Product Manufactor Cost:", "$", self.__manufactorCost, "CAD")
        print("")
        print("Amount of Product in stock:", self.__stockLevel, "Units")
        print("Estimated amount manufactored:", self.__estManufactoredMnthly, "Units")
        print("")

    #generate the sales each month using the random module 
    def salesEachMonth(self, RandomSales):
        salesMonthly = self.__estManufactoredMnthly + RandomSales
        return salesMonthly

    

        


