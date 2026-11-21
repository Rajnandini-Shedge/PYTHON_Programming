#accept number from user and print $ and * 

def Pattern(No):
    if No <= 0:
        No = -No

    for i in range(No):
        print( "$ * ",end=" ")

def main():
    Value = int(input("Enter the number : "))
    Pattern(Value)

if __name__ == "__main__":
    main()