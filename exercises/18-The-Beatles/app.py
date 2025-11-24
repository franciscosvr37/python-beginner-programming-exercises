# ✅↓ Write your code here ↓✅

def sing():
    coro = "let it be, "
    estrofa1 = "the will be an answer, "
    estrofa2 = "whisper words of wisdom, "
    for i in range(1,12):
       if i == 5 : print(estrofa1)
       elif i == 11 : print(estrofa2, "let it be" )
       else : print(coro)
   
sing()