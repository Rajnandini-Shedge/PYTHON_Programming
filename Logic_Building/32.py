#accept amount in us dollar and return its corresponding 
# 1$ = 70 rupees

def DollarToINR(No):
    return No * 70

def main():
    Value = int(input("Enter the number : "))
    Ret = DollarToINR(Value)
    print(f"Dollar to INR of {Value} :",Ret)

if __name__ == "__main__":
    main()