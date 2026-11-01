no=11

def Display():
    a=21      #Local Variable
    print("From Display:",no)
    print("From Display value of a is:",a)    

def Demo():
    print("From Demo:",no)
    print("From Display value of a is:",a)   #ERROR


Display()
Demo()