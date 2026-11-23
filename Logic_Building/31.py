#accept number from user and print $ and * 

def Pattern(No):
    if No <= 0:
        No = -No

    for i in range(No*2):
        if i < No:
            print(" * ",end = " ")
        else:
            print(" # ",end = " ") 


def Optimized(No):
    print((" * " * No)+(" # "*No))

def main():
    Value = int(input("Enter the number : "))
    Pattern(Value)
    Optimized(Value)

if __name__ == "__main__":
    main()