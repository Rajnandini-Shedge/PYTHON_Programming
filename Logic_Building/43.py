#Write a program which accept number from user and return the count of digits in between 3 and 7

def CountRange(No):

    if No < 0 :
        No = -No

    Count = 0
    Digit = 0

    while 0 < No :
        Digit = No % 10
        if Digit > 3 and Digit < 7 :
            Count = Count+1
        No = No // 10

    return Count



def main():
    Value = int(input("Enter the number : "))

    Ret = CountRange(Value)

    print("Number between 3 qnd 7 are : ",Ret)

if __name__ == "__main__":
    main()