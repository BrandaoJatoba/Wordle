import random as rd
import ColorCode as cc
import GameScreen as gc

def start_game():
# lista de variáveis de configuração para o loop principal do jogo
    MAX_ATTEMPTS = 5      # numero de tentativas permitidas
    current_attempt = 1   # variável que conta as tentativas
    word = select_word()  # palavra a ser descoberta
    game_over = False     # status do jogo
    victory = False       # condição de vitória alcançada
    guesses = []          # lista de tentativas anteriores
    warning = ""          # mensagem de erro ou outros avisos
# Loop Principal do jogo
    while not game_over:
        gc.draw_screen(word, guesses, victory, warning)
        warning = "" # Esvaziar mensagem de aviso é importante ao iniciar novo ciclo, senão mensagem se repetem.
        try:            
            guess = input(f"{current_attempt}ª Tentativa: ")

            if len(guess) < 5:
                raise Exception("Palpite muito pequeno. Use palavras de cinco letras.")
                      
            if len(guess) > 5:
                raise Exception("Palpite muito grande. Use palavras de cinco letras.")

            if guess.isalpha == False:
                raise Exception("Digite apenas letras.")
                
            if guess.islower == False:
                raise Exception("Digite apenas letras minúsculas.")
            
            guesses.append(guess)

            if (guess == word): 
                game_over = True
                victory = True

            current_attempt += 1

            if current_attempt > MAX_ATTEMPTS:
                game_over = True

        except Exception as message:
            warning = str(message)
        
        finally:
            if current_attempt == 5: warning += " Última Tentativa!"
            
# se o jogo acabou, isso é, game_over é True, desenha tela mais uma vez, printa mensagem final e encerra o gameloop
    gc.draw_screen(word, guesses, victory)
    if victory == False:
        print(f"\n    Você perdeu. A palavra era {word}\n")
    else:
        print("\n     Parebéns. Você acertou.\n")
    pass

def select_word(): #seleciona palavra aleatória da lista fornecida
#OPORTUNIDADE DE UPDATE: FAZER COM QUE ESTA FUNÇÃO RECEBA UM NUMERO INTEIRO E ESCOLHA UMA PALAVRA COM ESTE TAMANHO...
    with open("_termo.txt", 'r') as list_of_words:
        list_of_all_words =list_of_words.readlines()
        size_of_list = len(list_of_all_words)
        selected_word_index = rd.randint(0, size_of_list)
        selected_word = list_of_all_words[selected_word_index]
        selected_word = selected_word.replace("\n", "")
    return selected_word


