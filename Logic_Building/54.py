#.Write a program which accept number from user and count frequency of 4 in it. 

def CountFour(No):

    if No < 0 :
        No = -No

    Count = 0
    Digit = 0

    while 0 != No :
        Digit = No % 10
        if Digit == 4 :
            Count = 1 + Count 
        No = No // 10

    return Count



def main():
    Value = int(input("Enter the number : "))

    Ret = CountFour(Value)

    print("Frequency of 4 is : ",Ret)

if __name__ == "__main__":
    main()