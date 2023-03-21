'''
@name: Analisador Lexico
@author: f5edy aaaaaaaaa
'''
from erros import print_errors
from lexico import get_token, print_tokens 
from datetime import datetime

start = datetime.now()

#concatenacao da entrada
codigo = ""
#controle do tempo de execucao
end_program = 0

#codigo a ser analisado
program_test = "exemplos_src/program2.txt"

#controle da sequencia 
tamanho = 0

def main():
    global codigo, start, end_program, tamanho
    print("Iniciando main...")

    print("\n------------- F5 COMPILER -------------")

    with open(program_test, 'r') as reader:
        # Read & print the entire file
        codigo = reader.read()
        print("\n------------------- Código -------------------\n" + codigo)

    # while end_program != 1:
    print("\n------------------- Análise Léxica -------------------")

    codigo_list = list(codigo)
    codigo_list.append(" ")
    
    for i in range(len(codigo_list)):
        #print("\ncaractere analisado: " + codigo_list[i] + " / estado: " + string_classes.mc_state)
        get_token(character=codigo_list[i], num_character=i)
    
    #print("\nToken mais recente: " + str(string_classes.token[len(string_classes.token)-1]))
    print_errors(program_test)            
    print_tokens()
    print_time()

        # end_program = 1

#NOTE calcula e printa o tempo de execucao
def print_time():
    global start

    print("\n----------Tempo----------")

    time_passed = datetime.now() - start
    print("\nTempo decorrido na análise: " + str(time_passed) + " milisegundos!\n\n")

if __name__ == "__main__":
    main()
