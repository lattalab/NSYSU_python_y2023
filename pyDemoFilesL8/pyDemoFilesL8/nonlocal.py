print ("\t msg1\t msg2\t msg3\t d")
msg1 = "glob";msg2 = "glob";msg3 = "glob";d={"G":0}
def topLv():
   msg1="topLv";msg2="topLv";msg3="topLv";d["T"] = 1
   def midLv():
      msg1="midLv";msg2="midLv";msg3="midLv";d["M"] = 2
      def botLv():
         global msg1
         nonlocal msg2
         msg1="botLv";msg2="botLv";msg3="botLv";d["B"] = 3
         print("B:\t",msg1,"\t",msg2,"\t",msg3,"\t",d)
      botLv()
      print("M:\t",msg1,"\t",msg2,"\t",msg3,"\t",d)
   midLv()
   print("T:\t",msg1,"\t",msg2,"\t",msg3,"\t",d)
topLv()
print("G:\t",msg1,"\t",msg2,"\t",msg3,"\t",d)
