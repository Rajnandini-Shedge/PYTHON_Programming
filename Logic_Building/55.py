#Write a program which accept number from user and
#count frequency of such a digits which are less than 6. 

def Count(No):

    if No < 0 :
        No = -No

    Count = 0
    Digit = 0

    while 0 != No :
        Digit = No % 10
        if Digit < 6 :
            Count = 1 + Count 
        No = No // 10

    return Count



def main():
    Value = int(input("Enter the number : "))

    Ret = Count(Value)

    print("Frequency of numbers less than 6 are : ",Ret)

if __name__ == "__main__":
    main()