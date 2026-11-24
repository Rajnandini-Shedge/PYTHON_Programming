#Accept height and width and find rectangles area

def KMToMeter(Kilometer,meter= 1000):
    return Kilometer*meter

def main():
    Value1 = float(input("Enter the kilometer :  "))
    
    Ret = KMToMeter(Value1)

    print(f"{Value1} Km is equal to {Ret} meter ")

if __name__ == "__main__":
    main()