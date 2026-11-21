#accept number from user and print number line  

def Display(No):
    if No <= 0:
        No = -No

    for i in range(-No ,No+1):
        print( i ,end=" ")

def main():
    Value = int(input("Enter the number : "))
    Display(Value)

if __name__ == "__main__":
    main()