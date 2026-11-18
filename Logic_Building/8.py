#Accept number from user 
# <= 10 Hello
# > 10 Demo
def Display(No):
    if No <= 10:
        print("HEllo")
    else:
        print("Demo")
        
def main():
    Value = int(input("Enter the number : "))
    Display(Value)

if __name__ == "__main__":
    main()