import deck
face = ' ⓐ②③④⑤⑥⑦⑧⑨⑩ⓙⓠⓚ'
suit = '♧♡♤♢'
print(face[deck.cards[deck.p]%14]+suit[deck.cards[deck.p]//14],end=" ")
deck.p+=1
