#Accept radius and find its area

def CircleArea(Rad,PI = 3.14):
    return Rad * Rad * PI

def main():
    Value = float(input("Enter the radius :  "))

    Ret = CircleArea(Value)

    print("Area of circle is : ",Ret)

if __name__ == "__main__":
    main()