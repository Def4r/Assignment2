import random
from UserChecking import userVI

class ProductClass:
    
    def __init__(self, productName = "", productCode = 0, productSalesPrice = 0, manufactorCost = 0, stockLevel = 0, estManufactoredMnthly = 0):
        self.__productName = productName
        self.__productCode = productCode
        self.__productSalesPrice = productSalesPrice
        self.__manufactorCost = manufactorCost
        self.__stockLevel = stockLevel
        self.__estManufactoredMnthly = estManufactoredMnthly

    #def userV(self, inputP, MinInt, MaxInt):
     #   while true:
      #      try:
       #         num = int(input(inputP))
        #        if MinInt <= num <= MaxInt:
         #           return num
          #      else:
           #         print("Input must be between ", MinInt, " and ", MaxInt, "Try Again.")
            #except ValueError:
             #   print("Input recieved is not vaild. Try again.")

    def BusinessInfo(self):
        self.__productName = input("Whats is the name of your product? :>")
        self.__productCode = userVI("What is the code for your product? :>", 100, 1000)
        self.__productSalesPrice = userVI("How much would you price your products? CAD ONLY :>", 0, 100000000)
        self.__manufactorCost = userVI("How much does it cost to make your product? :>", 0, 10000000)
        self.__stockLevel = userVI("How much do you currently have in your stock?", 0, 100000000)
        self.__estManufactoredMnthly = userVI("How much do you manufactor every month. This is an Estimate. :>", 0, 10000000)

    def salesEachMonth(self, salesMonthly):
        randomInc = random.randint(-10 , 10)
        salesMonthly = self.__estManufactoredMnthly + randomInc
        return salesMonthly

    

        


