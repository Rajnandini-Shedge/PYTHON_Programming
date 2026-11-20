#Display summation non-Factors of given number

def DisplayNonFactor(No):
    if No <= 0:
        No = -No

    Sum = 0 
    for i in range(1 , No):
        if( No  % i != 0 ):
            Sum = Sum + i

    return Sum 

def main():
    Value = int(input("Enter Number : "))
    Ret = DisplayNonFactor(Value)
    print("Summation of non-factor is : ",Ret)
if __name__ == "__main__":
    main()