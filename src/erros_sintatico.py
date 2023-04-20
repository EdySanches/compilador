'''
    @author: f5edy
    @description: catch errors from sintatic analyse
'''

# libs
from sintatico import sint_erro

# globais
error = sint_erro

# verifica e mostra os erros
def print_sint_errors():
    global error

    print("\n----------Erros----------")

    #variaveis
    num_linha = 0

    #listagem dos erros    
    cont_erros = len(error)
    print("Total de erros: " + str(cont_erros) + "\n")

    if len(error) > 0:
        for i in range(len(error)):
            print(f"Erro: {error[i][0]}. No caracter [{error[i][1]}]. \n" + 
                  f"Esperado: {error[i][2][0]} | Presente: {error[i][2][1]}. \n" )
