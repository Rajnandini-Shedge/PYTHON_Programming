def PrintEven(No):
    if No <= 0:
        return

    for i in range(1,No+1):
        Even = i * 2
        print(Even , end = ' ')

def main():

    Value = int(input("Enter Number : "))
    PrintEven(Value)

if __name__ == "__main__":
    main()