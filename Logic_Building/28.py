#Find factorial of program
# 5  = (5 * 4* 3* 2* 1)
# 120

def Factorial(No):
    if No < 0:
        No = -No

    Fact = 1

    for i in range(No,0,-1):
        Fact = i * Fact
        
    return Fact

def main():
    Value = int(input("Enter the number :"))

    Ret = Factorial(Value)

    print(f"Factorial of {Value} is ",Ret)

if __name__ == "__main__":
    main()