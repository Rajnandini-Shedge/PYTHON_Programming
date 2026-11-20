#Display diff between factor and non-Factors of given number

def DisplayNonFactor(No):
    if No <= 0:
        No = -No

    Sum1= 0
    Sum2 = 0 
    for i in range(1 , No):
        if( No  % i == 0 ):
            Sum1 = Sum1 + i
        else :
            Sum2 = Sum2 + i

    return Sum1-Sum2

def main():
    Value = int(input("Enter Number : "))
    Ret = DisplayNonFactor(Value)
    print("Difference of factor and non-factor is : ",Ret)
if __name__ == "__main__":
    main()