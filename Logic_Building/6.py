def Display(No):
    i = 0
    while i < No:
        print("*")
        i = i + 1

def main():
    Value = int(input("Enter the numner : "))
    Display(Value)

if __name__ == "__main__":
    main()