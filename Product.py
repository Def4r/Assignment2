import random

class ProductClass:
    
    def __init__(self, productName = "", productCode = 0, productSalesPrice = 0, manufactorCost = 0, stockLevel = 0, estManufactoredMnthly = 0):
        self.__productName = productName
        self.__productCode = productCode
        self.__productSalesPrice = productSalesPrice
        self.__manufactorCost = manufactorCost
        self.__stockLevel = stockLevel
        self.__estManufactoredMnthly = estManufactoredMnthly

    def userVaild(inputP, MinInt, MaxInt):
        while true:
            try:
                num = int(input(inputP))
                if MinInt <= num <= MaxInt:
                    return num

    def BusinessInfo(self):
        self.__productName = input("Whats is the name of your product? :>")
        self.__productCode = int(input("What is the code for your product? :>"))
        self.__productSalesPrice = int(input("How much would you price your products? CAD ONLY :>"))
        self.__manufactorCost = int(input("How much does it cost to make your product? :>"))
        self.__stockLevel = int(input("How much do you currently have in your stock?"))
        self.__estManufactoredMnthly = int(input("How much do you manufactor every month. This is an Estimate. :>"))

    def salesEachMonth(self, salesMonthly):
        randomInc = random.randint(-10 , 10)
        salesMonthly = self.__estManufactoredMnthly + randomInc
        return salesMonthly

    

        


