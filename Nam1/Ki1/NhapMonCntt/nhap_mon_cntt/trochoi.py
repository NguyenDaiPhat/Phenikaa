def play_game():
    secret_number = 7
    guess_number = int(input("Moi ban nhap vao mot so:"))
    if guess_number == secret_number:
        print("Chuc mung! Ban da chien thang")
    else: print("ban ngu the?")
from random import randint 
def play_game2():
   secret_number=randint(1,10)
   while True:
        guess_number=int(input("moi nhap: "))
        if guess_number== secret_number:
            print("ao qua, chuc mung m nhap dung doi")
            break
        elif guess_number<secret_number:
            print("m nhap be qua, nhap lai")
        else: print("m nhap to qua, nhap lai")
  
        
