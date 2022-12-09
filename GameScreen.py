import ColorCode as color
import os

def color_alphabet(word:str, list_of_guesses:list):    
    # Códigos das Cores para o Dicionário.
    # 0 = Sem cor.
    # 1 = Amarelo (Letra correta na posição errada).
    # 2 = Verde (Letra correta).
    # 3 = Vermelho (Letra não está na palavra.

    #dicionário com todas as letras será iterado e guardará a cor das letras a serem pintadas.
    alphabet =  { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "z": 0}
    
    i = 0 #contador que ajudará a iterar as letras na palavra misteriosa.

    if len(list_of_guesses)>0: #código abaixo só funciona a partir do primeiro palpite. 
        for each_guess in list_of_guesses:  #loop dos palpites.
            letters_in_word = {} # dicionário que guarda a quantidade de letras repetidas na palavra misteriosa. Será usado no loop das letras.
            for each_letter in word:
                letters_in_word.setdefault(each_letter, word.count(each_letter))
            for letter in each_guess:       #loop das letras
                counting = letters_in_word.get(word[i])
                # se a letra analisada está no lugar errado OU se há letra repetida mas não se acertou todas as letras, a letra será pintada de amarelo na barra ALFABETO
                if ((letter in word) and (letter != word[i])) or (letter == word[i] and counting > 1):
                    letters_in_word[letter] = word.count(letter)-1
                    alphabet[letter] = 1
                    i += 1
                    continue
                # se a letra está correta E todas as letras repetidas foram contabilizadas, a letra será pintada de verde na barra ALFABETO.
                elif letter == word[i] and counting <= 1:
                    alphabet[letter] = 2
                    i += 1                
                    continue
                # se a letra não está na palavra, ela será pintada de vermelho na barra ALFABETO.
                elif letter not in word:
                    alphabet[letter] = 3
                    i += 1
                    continue                
            i = 0 # o contador deve ser resetado ao final do loop interno (loop das letras), para que não haja erro ao iterar o próximo palpite no proximo loop de letras.
    alphabet_colored = ""
    #loop que de fato pinta as letras isoladamente e as junta num só string
    for letter in alphabet: 
        if alphabet[letter] == 0:
            alphabet_colored += "".join(letter + " ")
        elif alphabet[letter] == 1:
            alphabet_colored += "".join(color.YELLOW + letter + color.END + " ")
        elif alphabet[letter] == 2:
            alphabet_colored += "".join(color.GREEN + letter + color.END + " ")
        elif alphabet[letter] == 3:
            alphabet_colored += "".join(color.RED + letter + color.END + " ")        
    return alphabet_colored
 
def draw_screen(word:str, list_of_guesses:list, victory:bool, warning = ""):

    #primeiro limpar tela para não dar erro ao colorir
    os.system("CLS")
    #desenhar cabeçalho
    print("=============================================================")
    print(f"=                  "+color.BOLD+"Term.ooo"+color.END +" by João Jatobá                  =")
    print("=============================================================\n")
    print("=     " + color_alphabet(word, list_of_guesses)+"    =")
    print()
    print("=============================================================\n")
    print("             " + warning + "")
    #desenhar attempts até agora
    for guess in range(len(list_of_guesses)):
        if len(list_of_guesses) > 0:
            formatted_word = ""
            for index in range(len(word)):
                if (list_of_guesses[guess][index] in word) and (list_of_guesses[guess][index] != word[index]):
                    formatted_word += (color.YELLOW + list_of_guesses[guess][index] + color.END)
                    continue
                if (list_of_guesses[guess][index] in word) and (list_of_guesses[guess][index] == word[index]):
                    formatted_word += (color.GREEN  + list_of_guesses[guess][index] + color.END)
                    continue
                formatted_word += list_of_guesses[guess][index]
            print(f"{guess + 1}ª tentativa: {formatted_word}")
    pass
