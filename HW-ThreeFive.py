for num_list in range(1,101):
    if (num_list % 3 == 0) & (num_list % 5 == 0):
        print("ThreeFive")
    elif num_list % 3 == 0:
        print("Three")
    elif num_list % 5 == 0:
        print("Five")
    else:
        print(num_list)
