#.Write a program which accept number from user and return multiplication of all digits. 

def MultDigits(No):

    if No < 0 :
        No = -No

    Mult = 1
    Digit = 0

    while 0 != No :
        Digit = No % 10
        if Digit == 0 :
            Digit = 1
        Mult = Mult * Digit
        No = No // 10

    return Mult



def main():
    Value = int(input("Enter the number : "))

    Ret = MultDigits(Value)

    print("Multiplication of digit is : ",Ret)

if __name__ == "__main__":
    main()