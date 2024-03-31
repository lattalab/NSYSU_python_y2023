class CSE282():#A university class only becomes
               #real when some students join it
    handSpray=True
    def __init__(self,color):
        self.mask=color
        self.inRoom=True
    def removeMask(self):
        if self.inRoom:
            print("No"); return
        print("OK");self.mask=None
    def leaveRoom(self):
        if not self.inRoom:
            print("Already left."); return
        print("OK"); self.inRoom=False
    def useSpray(self,RememberToPutBack=True):
        if not self.inRoom:
            print("Already left."); return
        if CSE282.handSpray:
            print("Used.")
            self.used=True
            CSE282.handSpray=RememberToPutBack
        else: print("You can't. Someone took it.")

#We expect that some other classes would be defined here...
