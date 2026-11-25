#Write a program which accept number from user and return the count of odd digits.

def CountOdd(No):

    if No < 0 :
        No = -No

    Count = 0
    Digit = 0

    while 0 < No :
        Digit = No % 10
        if Digit % 2 != 0:
            Count = Count+1
        No = No // 10

    return Count



def main():
    Value = int(input("Enter the number : "))

    Ret = CountOdd(Value)

    print("count of Odd numbers are : ",Ret)

if __name__ == "__main__":
    main()