#Accept temp in fahrenheit and convert to celsius

def FhTOCs(temp):
    Cs = (temp - 32 ) * (5/9)
    return Cs

def main():
    Value1 = float(input("Enter the Temperature :  "))
    
    Ret = FhTOCs(Value1)

    print(f"{Value1} Fh is equal to {Ret} Celsius ")

if __name__ == "__main__":
    main()