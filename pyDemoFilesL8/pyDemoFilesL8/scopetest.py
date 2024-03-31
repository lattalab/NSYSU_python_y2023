a="g";b="g";c="g";d="g";e="g";f="g";g="g";h="h"
def side():
    g="s";h="s"
    side2()
    
def side2():
    print(a,b,c,d,e,f,g,h)
    
def top():
    b="t";c="t";d="t";e="t";f="t";g="t";h="t"
    def mid():
        c="m";d="m";e="m";f="m";g="m";h="m"
        def bot():
            global d
            nonlocal e
            f="b";g="b";h="b"
            print(a,b,c,d,e,f,g,h); side()
        bot(); print(a,b,c,d,e,f,g,h); side()
    mid(); print(a,b,c,d,e,f,g,h); side()
top(); print(a,b,c,d,e,f,g,h); side()
