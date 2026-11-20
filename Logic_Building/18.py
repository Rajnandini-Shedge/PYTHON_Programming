#Display all non-Factors of given number

def DisplayNonFactor(No):
    if No <= 0:
        No = -No

    for i in range(1 , No):
        if( No  % i != 0 ):
            print( i , end = ' ')

def main():
    Value = int(input("Enter Number : "))
    DisplayNonFactor(Value)

if __name__ == "__main__":
    main()