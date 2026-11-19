# Excpet Number from user and find its even factors and display
def DisplayFactor(No):
    if No <= 0:
        No = -No

    No1 = (No//2)+1
    for i in range(1 , No1):
        if( No  % i == 0 )and( i % 2 == 0) :
            print( i , end = ' ')

def main():
    Value = int(input("Enter Number : "))
    DisplayFactor(Value)

if __name__ == "__main__":
    main()