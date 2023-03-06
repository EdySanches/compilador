'''
@name: Analisador Lexico
@author: f5edy
'''
import erros
import string_classes
from datetime import datetime

start = datetime.now()

#concatenacao da entrada
codigo = ""
#controle do tempo de execucao
end_program = 0

#codigo a ser analisado
program_test = "analisador-lexico-main/program2.txt"

#controle da sequencia 
tamanho = 0

def main():
    global codigo, start, end_program, tamanho
    print("Iniciando main...")

    print("\n------------- ANALISADOR LÉXICO -------------")

    with open(program_test, 'r') as reader:
        # Read & print the entire file
        codigo = reader.read()
        print("\n-------------------Código-------------------\n" + codigo)

    while end_program != 1:
        print("\n------------------- Resultado da Compilação -------------------")

        cadeia_list = list(codigo)
        cadeia_list.append(" ")

        tamanho = len(cadeia_list)
        
        for i in range(tamanho):
            print("\ncaractere analisado: " + cadeia_list[i] + " / estado: " + string_classes.mc_state
                + " / tamanho: " + str(i))
            string_classes.get_token(character=cadeia_list[i], num_character=i)
        
        #print("\nToken mais recente: " + str(string_classes.token[len(string_classes.token)-1]))

        print_time()
        erros.print_erro()            
        string_classes.print_tokens()

        end_program = 1

#NOTE calcula e printa o tempo de execucao
def print_time():
    global start

    print("\n----------Tempo----------")

    time_passed = datetime.now() - start
    print("\nTempo decorrido na análise: " + str(time_passed) + " milisegundos!")

if __name__ == "__main__":
    main()
