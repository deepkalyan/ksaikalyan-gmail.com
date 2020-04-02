
no_of_games = input("Enter how many number of games")
print(no_of_games)
ref=15
for i in range(0,int(no_of_games)):
    num = input("select one number from range of 1 to 25")
    print(num)
    if int(num)>ref:
        print("random number is higher")
    elif int(num)<ref:
        print("random number is lower")
    elif int(num) == ref:
        print("guess is right")
        print("your guess is right in " + str(i) +"st  iteration")
    
