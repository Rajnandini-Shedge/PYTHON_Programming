# Write a program which accept range from user and return addition of all numbers in between that range. (Range should contains positive numbers only) 

def RangeSum(No1,No2):

    if No1 > No2 or No1 < 0:
            return -1 

    Sum = 0
    for i in range(No1,No2+1):
        Sum = Sum + i

    return Sum

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
        
    Ret = RangeSum(Value1, Value2)
    if Ret == -1:
        print("Invalid Range")
    else:
        print("Addition of given range is : ", Ret)

if __name__ == "__main__":
    main()