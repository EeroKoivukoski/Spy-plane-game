def numerochecker(y,z):
   z+=1
   while True:
        try:
            int(y)
        except ValueError:
            print("That's not a number!")
        else:
            y = int(y)
            for i in range(1, z):
                if y == i:
                    return y
        y=input("Enter the input: ")