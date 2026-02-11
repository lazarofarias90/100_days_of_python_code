import random

lista_de_numeros = []

for i in range(1, 101):
    lista_de_numeros.append(i)

numero_escolhido = random.choice(lista_de_numeros)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
dificuldade_escolhida = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()

def guess_game(num_mode):

    tentativas = num_mode

    while tentativas > 0:
        
        print(f"You have {tentativas} attempts remaining to guess the number")
        aposta = int(input("Make a guess: "))
        
        if aposta != numero_escolhido:
            if aposta > numero_escolhido:
                print("Too high!")
                print("Guess again.")
            else:
                print("Too low!")
                print("Guess again.")
            tentativas -= 1
        else:
            print("Congratulations! You choose the right number!")
            break

if dificuldade_escolhida == "easy":
    guess_game(10)
else:
    guess_game(5)