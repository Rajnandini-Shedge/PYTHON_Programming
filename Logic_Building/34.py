# Write a program to find odd factorial of given number.  

def OddFact(No):

    if No < 0:
        No = -No

    fact = 1
    for i in range(1,No+1):
        if i % 2 != 0:
            fact = fact*i
            
    return fact

def main():
    Value = int(input("Enter the number : "))
    Ret = OddFact(Value)

    print("Multiplication of odd factorials : ",Ret)

if __name__ == "__main__":
    main()