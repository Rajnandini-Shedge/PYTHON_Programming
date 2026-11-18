def Display(No):
    i = 0
    while i < No:
        print("*")
        No = No - 1

def main():
    Value = int(input("Enter the number : "))
    Display(Value)

if __name__ == "__main__":
    main()