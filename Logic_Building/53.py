#.Write a program which accept number from user and count frequency of 2 in it. 

def CountTwo(No):

    if No < 0 :
        No = -No

    Count = 0
    Digit = 0

    while 0 != No :
        Digit = No % 10
        if Digit == 2 :
            Count = 1 + Count 
        No = No // 10

    return Count



def main():
    Value = int(input("Enter the number : "))

    Ret = CountTwo(Value)

    print("Frequency of 2 is : ",Ret)

if __name__ == "__main__":
    main()