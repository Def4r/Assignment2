#This file is were all the user checks will be stored, From here it can be imported into the files were its needed to make the code cleaner.

#This function takes in a max and min and user must enter an int between these ranges. Used only for the product code
def userVI(inputP, MinInt, MaxInt):
    while True:
        try:
            num = int(input(inputP))
            if MinInt <= num <= MaxInt:
                return num
            else:
                print("Input must be between ", MinInt, " and ", MaxInt, "Try Again.")
        except ValueError:
            print("Input recieved is not vaild. Try again.")
        
#This function is takes in only a min and the user must enter int greater than the min value
def userVII(inputP, MinInt):
    while True:
        try:
            num = int(input(inputP))
            if num > MinInt:
                return num
            else:
                print("Input must be greater than ", MinInt, " Try Again.")
        except ValueError:
            print("Input recieved is not vaild. Try again.")

#Very simliar to the second function but this one must be greater than or equal to the int given in.
def userVIII(inputP, MinInt):
    while True:
        try:
            num = int(input(inputP))
            if num >= MinInt:
                return num
            else:
                print("Input must be between greater than or equals to ", MinInt, " Try Again.")
        except ValueError:
            print("Input recieved is not vaild. Try again.")


