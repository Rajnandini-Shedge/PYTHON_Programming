def Display(No,pattern):
    for i in range(No):
        print(pattern)

def main():
    Value = int(input("Enter Number to display :")) 
    Pattern = input("Enter  pattern :")
    Display(Value , Pattern)

if  __name__ == "__main__":
    main()