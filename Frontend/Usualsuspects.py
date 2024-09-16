def numerochecker(y):
   while True:
        try:
            int(y)
        except ValueError:
            print("That's not a number!")
        else:
            y = int(y)
            if y == 1 or y == 2:
                return y
        y=input("Enter the input: ")