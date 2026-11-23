#.Write a program to find even factorial of given number. 

def EvenFact(No):

    if No < 0:
        No = -No

    fact = 1
    for i in range(1,No+1):
        if i % 2 == 0:
            fact = fact*i
            
    return fact

def main():
    Value = int(input("Enter the number : "))
    Ret = EvenFact(Value)

    print("Multiplication of even factorials : ",Ret)

if __name__ == "__main__":
    main()