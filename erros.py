#NOTE bibliotecas
from main import program_test
from string_classes import erro, coment_aberto, parenteses_aberto, begin_aberto

#NOTE verifica e mostra os erros
def print_erro():
    global erro, coment_aberto, parenteses_aberto, begin_aberto

    print("\n----------Erros----------")

    #variaveis
    num_linha = 0
    erro  = erro
    coment_aberto = coment_aberto
    parenteses_aberto = parenteses_aberto
    begin_aberto = begin_aberto

    #erro de encapsulamento de comentarios
    if (len(coment_aberto) > 0) or (len(parenteses_aberto) > 0) or (len(begin_aberto) > 0):
        for j in range(len(coment_aberto)):
            erro.append(["coment_aberto",coment_aberto[j]])
        for j in range(len(parenteses_aberto)):
            erro.append(["coment_aberto",parenteses_aberto[j]])
        for j in range(len(begin_aberto)):
            erro.append(["coment_aberto",begin_aberto[j]])        

    #listagem dos erros    
    cont_erros = len(erro)
    print("Total de erros: " + str(cont_erros) + "\n")

    if len(erro) > 0:
        for i in range(len(erro)):
            num_linha = search_line(i)
            print("Erro " +  str(erro[i][0]) + ". Line[" + str(num_linha) + "]. Cl[" + str(erro[i][1]) + "]."
             + " Ch[" + str(erro[i][2]) + "].\n" )

#NOTE calcula e mostra a linha do erro
def search_line(num_character):
    linha = ""
    linha_erro = -1
    num_caract_linha = 0
    soma_num_caract_linha = 0

    num_linha = sum(1 for line in open(program_test))

    with open(program_test, 'r') as reader:
        for i in range(num_linha):
            linha = reader.readline(num_linha)
            num_caract_linha = len(linha)
            soma_num_caract_linha = soma_num_caract_linha + num_caract_linha
            
            if soma_num_caract_linha > int(num_character):
                linha_erro = num_linha
            
    return linha_erro         
