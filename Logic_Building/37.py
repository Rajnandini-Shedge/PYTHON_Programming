#Accept height and width and find rectangles area

def RectArea(Width,Height):
    return Width*Height

def main():
    Value1 = float(input("Enter the Width :  "))
    Value2 = float(input("Enter the Height :  "))
    
    Ret = RectArea(Value1, Value2)

    print("Area of Rectangle is : ",Ret)

if __name__ == "__main__":
    main()