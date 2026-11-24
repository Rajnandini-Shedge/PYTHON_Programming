# Write a program which accept area in square feet and convert it into square meter. (1 square feet = 0.0929 Square meter) 

def SquareMeter(No):
    return No * 0.0929
        
def main():
    Value = int(input("Enter the number : "))
    Ret = SquareMeter(Value)

    print(f"{Value} Squatr feet to {Ret} square meter.")

if __name__ == "__main__":
    main()