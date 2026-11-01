no=11

def Display():
    global no     #refer global no
    no=21         # so 21 is overwritten on 11
    print("From Display : ",no)        #2s 1

print("Before:",no)     #11
Display()
print("After:",no)       #21