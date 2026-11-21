#accept number from user and print numbers till that number 

def Display(No):
    if No <= 0:
        No = -No

    for i in range(1,No+1):
        print( i ,end=" ")

def main():
    Value = int(input("Enter the number : "))
    Display(Value)

if __name__ == "__main__":
    main()