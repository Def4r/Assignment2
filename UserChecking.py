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

def userVIII(inputP, MinInt):
    while True:
        try:
            num = int(input(inputP))
            if num >+ MinInt:
                return num
            else:
                print("Input must be between greater than or equals to ", MinInt, " Try Again.")
        except ValueError:
            print("Input recieved is not vaild. Try again.")


