'''
@name: Analisador Lexico
@author: f5edy
'''

# libs
from datetime import datetime
from erros_lexico import print_lex_errors
from lexico import get_lex_token, print_lex_tokens 
from sintatico import get_sint_token, print_sint_tokens
from erros_sintatico import print_sint_errors

# globais
#controle de tempo
start = datetime.now()
#concatenacao da entrada
codigo = ""
#controle do tempo de execucao
end_program = 0
#codigo a ser analisado
program_test = "exemplos_programs/program3.txt"
#controle da sequencia 
tamanho = 0
#controle de tokens
lex_tokens = []
sint_tokens = []

#NOTE principal
def main():
    global codigo, start, end_program, tamanho, lex_tokens
    print("Iniciando main...")

    print("\n----------------------- COMPILADOR -----------------------")

    # abrindo codigo fonte
    with open(program_test, 'r') as reader:
        codigo = reader.read()
        print("\n------------------- Código -------------------\n" + codigo)

    print("\n-------------------   Análise Léxica   -------------------")
    codigo_list = list(codigo)
    codigo_list.append(" ")
    
    for i in range(len(codigo_list)):
        #print("\ncaractere analisado: " + codigo_list[i] + " / estado: " + string_classes.mc_state)
        get_lex_token(character=codigo_list[i], num_character=i, lex_tokens=lex_tokens)
    
    #print("\nToken mais recente: " + str(string_classes.token[len(string_classes.token)-1]))
    print_lex_errors(program_test)            
    print_lex_tokens(lex_tokens)
    lex_tokens.append(" ") 

    print("\n------------------- Análise Sintática -------------------")
    get_sint_token(lex_tokens=lex_tokens, sint_tokens=sint_tokens)
    print_sint_errors()
    print_sint_tokens(sint_tokens)

    print("\n-------------------       Tempo       -------------------")
    print_comp_time()


#NOTE calcula e printa o tempo de execucao
def print_comp_time():
    global start

    tempo = datetime.now() - start
    print("\nTempo decorrido na análise: " + str(tempo) + " milisegundos!\n\n")


if __name__ == "__main__":
    main()
