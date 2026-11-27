#Write a program which accept number from user and display its digits in reverse order. 

def DisplayDigits(No):

    if No < 0 :
        No = -No

    Digit = 0

    while 0 != No :
        Digit = No % 10
        print(Digit)
        No = No // 10

def main():
    Value = int(input("Enter the number : "))

    DisplayDigits(Value)


if __name__ == "__main__":
    main()