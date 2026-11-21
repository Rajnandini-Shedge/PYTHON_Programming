#accept number from user and print odd number  

def DisplayOdd(No):
    if No <= 0:
        No = -No

    for i in range(No+1):
        if i % 2 != 0:
            print( i ,end=" ")

def main():
    Value = int(input("Enter the number : "))
    DisplayOdd(Value)

if __name__ == "__main__":
    main()