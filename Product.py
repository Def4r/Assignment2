import random

class ProductClass:

    NoLimit = float('inf')
    
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
                else:
                    print("Input must be between ", MinInt, " and ", MaxInt, "Try Again.")
            except ValueError:
                print("Input recieved is not vaild. Try again.")

    def BusinessInfo(self):
        self.__productName = input("Whats is the name of your product? :>")
        self.__productCode = userVaild("What is the code for your product? :>", 100, 1000)
        self.__productSalesPrice = userVaild("How much would you price your products? CAD ONLY :>", 0, NoLimit)
        self.__manufactorCost = userVaild("How much does it cost to make your product? :>", 0, NoLimit)
        self.__stockLevel = userVaild("How much do you currently have in your stock?", 0, NoLimit)
        self.__estManufactoredMnthly = userVaild("How much do you manufactor every month. This is an Estimate. :>", 0, NoLimit)

    def salesEachMonth(self, salesMonthly):
        randomInc = random.randint(-10 , 10)
        salesMonthly = self.__estManufactoredMnthly + randomInc
        return salesMonthly

    

        


