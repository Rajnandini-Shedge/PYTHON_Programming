#Write a program which accept number from user and return difference between summation of even digits and summation of odd digits.

def CountDiff(No):

    if No < 0 :
        No = -No

    CountEven = 0
    CountOdd = 0
    Digit = 0


    while 0 < No :
        Digit = No % 10
        if Digit % 2 == 0:
            CountEven = CountEven+Digit
        else:
            CountOdd = CountOdd+Digit
        No = No // 10

    return CountEven -CountOdd



def main():
    Value = int(input("Enter the number : "))

    Ret = CountDiff(Value)

    print("Difference of Odd and even numbers is : ",Ret)

if __name__ == "__main__":
    main()
