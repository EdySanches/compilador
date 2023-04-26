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

    #listagem dos erros    
    cont_erros = len(error)

    if len(error) > 0:
        print("Total de erros: " + str(cont_erros) + "\n")
        for i in range(len(error)):
            print(f"Erro: {error[i][0]}. No caracter [{error[i][2]}] de indice [{error[i][1]}]. \n" + 
                  f"Esperado: [{error[i][3]}] | Presente: [{error[i][2][0]}]. \n" )
    else:
        print("Nao ha erros no codigo!")