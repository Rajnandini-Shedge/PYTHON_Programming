# Display multiplication of factor of given number

def MultFact(No):
    if No <= 0:
        No = -No
    
    No1 = (No//2)+1
    Mult = 1 
    for i in range(1 , No1):
        if No  % i == 0 :
            Mult = Mult * i
    
    return Mult
    
    
def main():
    Value = int(input("Enter the number : "))

    Ret = MultFact(Value)

    print(f"{Value} Multiplication of factor is : ",Ret)
if __name__ == "__main__":
    main()