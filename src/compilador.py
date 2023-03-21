'''
@name: Analisador Lexico
@author: f5edy aaaaaaaaa
'''

# libs
from datetime import datetime
from sintatico import get_sint_token
from erros_lexico import print_lex_errors
from lexico import get_lex_token, print_lex_tokens 

# globais
#controle de tempo
start = datetime.now()
#concatenacao da entrada
codigo = ""
#controle do tempo de execucao
end_program = 0
#codigo a ser analisado
program_test = "exemplos_src/program2.txt"
#controle da sequencia 
tamanho = 0
#controle de tokens
lex_tokens = []
sint_tokens = []

#NOTE calcula e printa o tempo de execucao
def print_lex_time():
    global start

    print("\n----------Tempo----------")

    time_passed = datetime.now() - start
    print("\nTempo decorrido na análise: " + str(time_passed) + " milisegundos!\n\n")

#NOTE principal
def main():
    global codigo, start, end_program, tamanho, lex_tokens
    print("Iniciando main...")

    print("\n------------- F5 COMPILER -------------")

    # abrindo codigo fonte
    with open(program_test, 'r') as reader:
        codigo = reader.read()
        print("\n------------------- Código -------------------\n" + codigo)

    print("\n------------------- Análise Léxica -------------------")

    codigo_list = list(codigo)
    codigo_list.append(" ")
    
    for i in range(len(codigo_list)):
        #print("\ncaractere analisado: " + codigo_list[i] + " / estado: " + string_classes.mc_state)
        get_lex_token(character=codigo_list[i], num_character=i, lex_tokens=lex_tokens)
    
    #print("\nToken mais recente: " + str(string_classes.token[len(string_classes.token)-1]))
    print_lex_errors(program_test)            
    print_lex_tokens(lex_tokens)
    print_lex_time()

    print("\n------------------- Análise Sintática -------------------")

    lex_tokens.append(" ")
    for j in range(len(lex_tokens)):
        get_sint_token(token_analisado=lex_tokens[j], num_character=j, sint_token=sint_tokens)


if __name__ == "__main__":
    main()
