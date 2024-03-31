from time import sleep
from random import shuffle
RPS=["Rock", "Paper", "Scissors"]
print("    ","✊✋✌ "*6)
print("     ★  Rock,  Paper,  Scissors,  Go!  ★")
print("    ","🥔🗋✀ "*7,end="\n\n\n")
sleep(1); print("\tRock...")
sleep(1); print("\tPaper...")
sleep(1); print("\tScissors...");sleep(1)
shuffle(RPS) #隨機排列
you=input("\tGo [RPS]: ")
print("\tI chose: ",RPS[0])
