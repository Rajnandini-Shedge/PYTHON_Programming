#Write a program which accept number from user and check whether it contains 0 in it or not. 

def ChkZero(No):

    if No < 0 :
        No = -No

    Digit = 0

    while 0 != No :
        Digit = No % 10
        if Digit == 0 :
            return True
        No = No // 10

    return False

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkZero(Value)

    if Ret == True:
        print("It Contains zero")
    else:
        print("There is no zero")


if __name__ == "__main__":
    main()