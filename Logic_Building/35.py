#  Write a program which returns difference between
# Even factorial and odd factorial of given number.  
def FactDiff(No):

    if No < 0:
        No = -No

    factEven = 1
    factOdd = 1
    for i in range(1,No+1):
        if i % 2 == 0:
            factEven = factEven * i 
        else:
            factOdd = factOdd * i
            
    return factEven -factOdd

def main():
    Value = int(input("Enter the number : "))
    Ret = FactDiff(Value)

    print("Difference of even and off factorial is : ",Ret)

if __name__ == "__main__":
    main()