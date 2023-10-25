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
