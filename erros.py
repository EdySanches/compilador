#NOTE bibliotecas
# from compilador import program_test
from string_classes import erro, coment_aberto, parenteses_aberto, begin_aberto

error = erro
#NOTE verifica e mostra os erros
def print_errors(src_file):
    global error, coment_aberto, parenteses_aberto, begin_aberto

    print("\n----------Erros----------")

    #variaveis
    num_linha = 0
    coment_aberto = coment_aberto
    parenteses_aberto = parenteses_aberto
    begin_aberto = begin_aberto

    #erro de encapsulamento de comentarios
    if (len(coment_aberto) > 0) or (len(parenteses_aberto) > 0) or (len(begin_aberto) > 0):
        for j in range(len(coment_aberto)):
            error.append(["coment_aberto",coment_aberto[j]])
        for j in range(len(parenteses_aberto)):
            error.append(["coment_aberto",parenteses_aberto[j]])
        for j in range(len(begin_aberto)):
            error.append(["coment_aberto",begin_aberto[j]])        

    #listagem dos erros    
    cont_erros = len(error)
    print("Total de erros: " + str(cont_erros) + "\n")

    if len(error) > 0:
        for i in range(len(error)):
            num_linha = search_line(src_file, i)
            print("Erro " +  str(error[i][0]) + ". Line[" + str(num_linha) + "]. Cl[" + str(error[i][1]) + "]."
             + " Ch[" + str(error[i][2]) + "].\n" )

#NOTE calcula e mostra a linha do erro
def search_line(src_file, num_char_errado):
    linha = ""
    linha_erro = -1
    num_caract_linha = 0
    soma_num_caract_linha = 0

    num_linha = sum(1 for line in open(src_file))

    with open(src_file, 'r') as reader:
        for i in range(num_linha):
            linha = reader.readline(num_linha)
            num_caract_linha = len(linha)
            soma_num_caract_linha = soma_num_caract_linha + num_caract_linha
            
            if soma_num_caract_linha > int(num_char_errado):
                linha_erro = num_linha
            
    return linha_erro         
