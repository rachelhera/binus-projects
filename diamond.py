size=int(input("Enter the length of the diamond:"))
x=0
y=int(size/2)+1
for i in range(0,size):
    number0fStars=i+1
    number0fSpaces = size - number0fStars
    for j in range(0,number0fSpaces):
        print(" ",end="")
    for k in range(0,number0fStars+x):
        print("*",end="")
    x=x+1
    print("\n")
for p in range(0,size):
    no0fSpaces=p+1
    no0fStars=size-no0fSpaces
    for q in range(0,no0fSpaces):
        print(" ",end="")
    for v in range(0,no0fStars+y):
        print("*",end="")
    y=y-1
    print("\n")
