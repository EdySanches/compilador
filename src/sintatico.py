# nao-terminais sao funcoes e terminais sao ifs

# libs
from palavras_reservadas import reserved_words
from lexico import is_ident

# from inspect import currentframe  #TODO ver isso ai
# globais
total_tokens = 0
idx_token = 0

sint_erro = []
seq_sint_tokens = []
res_words = reserved_words

# nao terminais
def get_sint_token(lex_tokens, sint_tokens):
    global total_tokens, idx_token, sint_erro

    # auxiliares
    seq_sint_tokens = []
    expectativa = ""
    total_tokens = len(lex_tokens)
    aux_idx_token = 0

    # analise de 'program'
    token_atual = lex_tokens[idx_token]
    expectativa = "program"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"{get_sint_token.__name__} -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token += 1
        token_atual = lex_tokens[idx_token]

        expectativa = "ident"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"{get_sint_token.__name__} -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1
            token_atual = lex_tokens[idx_token]

            expectativa = ";"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"{get_sint_token.__name__} -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

                idx_token += 1
                aux_idx_token = corpo(idx_token, lex_tokens, sint_tokens)

                idx_token = aux_idx_token
                token_atual = lex_tokens[idx_token]
                expectativa = "."
                if expectativa in token_atual:
                    seq_sint_tokens.append(token_atual[0])
                    print(f"{get_sint_token.__name__} -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
                    idx_token += 1
                    token_atual = lex_tokens[idx_token]
                    sint_tokens.append([seq_sint_tokens, "programa"])

                    # seq_sint_tokens.clear()

                else:
                    sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                    print(f"{get_sint_token.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                print(f"{get_sint_token.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"{get_sint_token.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"{get_sint_token.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    return idx_token
    

def corpo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    lex_tokens = lex_tokens

    aux_idx_token = 0
    aux_idx_token = dc(idx_token, lex_tokens, sint_tokens)
    
    idx_token = aux_idx_token
    token_atual = lex_tokens[idx_token]
    
    expectativa = "begin"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"{corpo.__name__} -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token += 1
        aux_idx_token = comandos(idx_token, lex_tokens, sint_tokens)

        idx_token = aux_idx_token
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"{corpo.__name__} -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

            sint_tokens.append([seq_sint_tokens, "corpo"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"{corpo.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"{corpo.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    
    # print(f"{corpo.__name__} -- Debug - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
    return idx_token

def dc(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0
    
    aux_idx_token = dc_v(idx_token, lex_tokens, sint_tokens)
    idx_token = aux_idx_token
    aux_idx_token = dc_p(idx_token, lex_tokens, sint_tokens)
    idx_token = aux_idx_token

    token_atual = lex_tokens[idx_token]
    print(f"{dc.__name__} -- CAPTUROU TOKEN: ['{dc.__name__}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
    sint_tokens.append([seq_sint_tokens, "dc"])
    # seq_sint_tokens.clear()
    return idx_token


def dc_v(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0
    
    token_atual = lex_tokens[idx_token]
    expectativa = "var"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"{dc_v.__name__} -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

        idx_token += 1    
        aux_idx_token = variaveis(idx_token, lex_tokens, sint_tokens)

        idx_token = aux_idx_token
        token_atual = lex_tokens[idx_token]
        expectativa = ":"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"{dc_v.__name__} -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1 
            
            token_atual = lex_tokens[idx_token]
            expectativa = "tipo_var"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"{dc_v.__name__} -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
                idx_token += 1 
                token_atual = lex_tokens[idx_token]
            
                expectativa = ";"
                if expectativa in token_atual:
                    seq_sint_tokens.append(token_atual[0])
                    print(f"{dc_v.__name__} -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
                    idx_token += 1 
                    aux_idx_token = dc_v(idx_token, lex_tokens, sint_tokens)
                    idx_token = aux_idx_token
                    sint_tokens.append([seq_sint_tokens, "dc_v"])

                else:
                    sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                    print(f"{dc_v.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                print(f"{dc_v.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"{dc_v.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        print(f"{dc_v.__name__} -- Sucesso na comparacao: ['null'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "dc_v"])
        # seq_sint_tokens.clear()
    return idx_token

#         seq_sint_tokens.append(expectativa) #TODO implementar essa logica de expectativa em todos.

def variaveis(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 00
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"{variaveis.__name__} -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

        idx_token += 1
        aux_idx_token = mais_var(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        sint_tokens.append([seq_sint_tokens, "variaveis"])
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"{variaveis.__name__} -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    return idx_token


def mais_var(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    aux_idx_token = 0    

    token_atual = lex_tokens[idx_token]
    expectativa = ","
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"mais_var -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token += 1
        aux_idx_token = variaveis(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token
        sint_tokens.append([seq_sint_tokens, "mais_var"])
        # seq_sint_tokens.clear()
    else:
        print(f"{mais_var.__name__} -- CAPTUROU TOKEN: ['{mais_var.__name__}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "mais_var"])
        # seq_sint_tokens.clear()
    return idx_token


def dc_p(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0
    
    token_atual = lex_tokens[idx_token]
    expectativa = "procedure"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"dc_p -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "ident"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"dc_p -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

            idx_token += 1
            aux_idx_token = parametros(idx_token, lex_tokens, sint_tokens)

            idx_token = aux_idx_token
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"dc_p -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
                idx_token += 1
                aux_idx_token = corpo_p(idx_token, lex_tokens, sint_tokens)
                idx_token = aux_idx_token
                aux_idx_token = dc_p(idx_token, lex_tokens, sint_tokens)
                idx_token = aux_idx_token

                sint_tokens.append([seq_sint_tokens, "dc_p"])
                # seq_sint_tokens.clear()
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                print(f"dc_p -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"dc_p -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        print(f"dc_v -- CAPTUROU TOKEN: ['dc_p'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "dc_p"])
        # seq_sint_tokens.clear()

    return idx_token


def parametros(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    aux_idx_token = 0

    token_atual = lex_tokens[idx_token]
    expectativa = "("
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"parametros -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

        idx_token += 1
        aux_idx_token = lista_par(idx_token, lex_tokens, sint_tokens)

        idx_token = aux_idx_token
        token_atual = lex_tokens[idx_token]
        expectativa = ")"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"parametros -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            sint_tokens.append([seq_sint_tokens, "parametros"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"parametros -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        print(f"parametros -- CAPTUROU TOKEN: ['parametros'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "parametros"])
        # seq_sint_tokens.clear()

    return idx_token


def lista_par(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    aux_idx_token = 0

    token_atual = lex_tokens[idx_token]
    aux_idx_token = variaveis(idx_token, lex_tokens, sint_tokens)

    idx_token = aux_idx_token
    token_atual = lex_tokens[idx_token]
    expectativa = ":"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"lista_par -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

        idx_token += 1
        # aux_idx_token = tipo_var(idx_token, lex_tokens, sint_tokens)
        token_atual = lex_tokens[idx_token]
        expectativa = "tipo_var"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"lista_par -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        
            idx_token = aux_idx_token
            aux_idx_token = mais_par(idx_token, lex_tokens, sint_tokens)
            idx_token = aux_idx_token

            sint_tokens.append([seq_sint_tokens, "lista_par"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"lista_par -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"lista_par -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    return idx_token


def mais_par(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = ";"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"mais_par -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token += 1
        aux_idx_token = lista_par(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token
        
        sint_tokens.append([seq_sint_tokens, "mais_par"])
        # seq_sint_tokens.clear()
    else:
        print(f"mais_par -- CAPTUROU TOKEN: ['mais_par'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "mais_par"])
        # seq_sint_tokens.clear()

    return idx_token


def corpo_p(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0

    aux_idx_token = dc_loc(idx_token, lex_tokens, sint_tokens)
    idx_token = aux_idx_token

    token_atual = lex_tokens[idx_token]
    expectativa = "begin"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"corpo_p -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token += 1
        aux_idx_token = comandos(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"corpo_p -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"corpo_p -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
                sint_tokens.append([seq_sint_tokens, "corpo_p"])
                # seq_sint_tokens.clear()

            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                print(f"corpo_p -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"corpo_p -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"corpo_p -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    return idx_token


def dc_loc(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0

    aux_idx_token = dc_v(idx_token, lex_tokens, sint_tokens)
    idx_token = aux_idx_token

    token_atual = lex_tokens[idx_token]
    print(f"dc_loc -- CAPTUROU TOKEN: ['dc_loc'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
    sint_tokens.append([seq_sint_tokens, "dc_loc"])
    # seq_sint_tokens.clear()

    return idx_token


def lista_arg(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(token_atual[0])

    aux_idx_token = 0
    
    token_atual = lex_tokens[idx_token]
    expectativa = "("
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"lista_arg -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token+=1
        aux_idx_token = argumentos(idx_token, lex_tokens, sint_tokens)
        
        idx_token = aux_idx_token
        token_atual = lex_tokens[idx_token]
        expectativa = ")"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"lista_arg -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            sint_tokens.append([seq_sint_tokens, "lista_arg"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"lista_arg -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    else:
        print(f"lista_arg -- CAPTUROU TOKEN: ['lista_arg'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "lista_arg"])
        # seq_sint_tokens.clear()

    return idx_token


def argumentos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(token_atual[0])
    
    aux_idx_token = 0
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"argumentos -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token+=1
        aux_idx_token = mais_ident(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        sint_tokens.append([seq_sint_tokens, "argumentos"])
        # seq_sint_tokens.clear()

    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"lista_arg -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    return idx_token



def mais_ident(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(token_atual[0])

    aux_idx_token = 0
    
    token_atual = lex_tokens[idx_token]
    expectativa = ";"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"lista_arg -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token+=1
        aux_idx_token = argumentos(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        sint_tokens.append([seq_sint_tokens, "mais_ident"])
        # seq_sint_tokens.clear()

    else:
        print(f"mais_ident -- CAPTUROU TOKEN: ['mais_ident'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")        
        sint_tokens.append([seq_sint_tokens, "mais_ident"])
        # seq_sint_tokens.clear()

    return idx_token



def p_falsa(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "else"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"p_falsa -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token+=1
        aux_idx_token = cmd(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        sint_tokens.append([seq_sint_tokens, "p_falsa"])
        # seq_sint_tokens.clear()
    else:
        print(f"p_falsa -- CAPTUROU TOKEN: ['p_falsa'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "p_falsa"])
        # seq_sint_tokens.clear()

    return idx_token



def comandos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    aux_idx_token = 0

    token_atual = lex_tokens[idx_token]
    
    expectativa = ""
    if "read" or "write" or "while" or "if" or "begin" in token_atual or is_ident(lex_tokens, token_atual):
        # if is_ident(lex_tokens, token_atual): print("esse é")
        seq_sint_tokens.append(token_atual[0])
        print(f"comandos -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        aux_idx_token = cmd(idx_token, lex_tokens, sint_tokens) 
        
        idx_token = aux_idx_token
        token_atual = lex_tokens[idx_token]
        expectativa = ":"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"comandos -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1 
            aux_idx_token = comandos(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([seq_sint_tokens, "comandos"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"comandos -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        print(f"comandos -- CAPTUROU TOKEN: ['comandos'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "comandos"])
        # seq_sint_tokens.clear()

    return idx_token



def cmd(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0
    
    token_atual = lex_tokens[idx_token]

    expectativa = "read"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "("
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1 
            aux_idx_token = variaveis(idx_token, lex_tokens, sint_tokens)
        
            idx_token = aux_idx_token 
            token_atual = lex_tokens[idx_token]
            expectativa = ")"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"cmd -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
                sint_tokens.append([seq_sint_tokens, "cmd"])
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    
    elif "write" in token_atual:
        seq_sint_tokens.append("write")
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "("
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1 
            aux_idx_token = variaveis(idx_token, lex_tokens, sint_tokens)
        
            idx_token = aux_idx_token 
            token_atual = lex_tokens[idx_token]
            expectativa = ")"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"cmd -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
                sint_tokens.append([seq_sint_tokens, "cmd"])
                # seq_sint_tokens.clear()
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
                print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    
    elif "if" in token_atual:
        seq_sint_tokens.append("if")
        idx_token += 1 
        aux_idx_token = condicao(idx_token, lex_tokens, sint_tokens)
        
        idx_token = aux_idx_token
        token_atual = lex_tokens[idx_token]
        expectativa = "then"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1 
            aux_idx_token = cmd(idx_token, lex_tokens, sint_tokens)

            idx_token = aux_idx_token 
            aux_idx_token = p_falsa(idx_token, lex_tokens, sint_tokens)

            idx_token = aux_idx_token 

            print(f"cmd -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()

        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    elif "ident" in token_atual:
        seq_sint_tokens.append("ident")
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = ":="
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            idx_token += 1 
            aux_idx_token = expressao(idx_token, lex_tokens, sint_tokens)
            idx_token = aux_idx_token

            print(f"cmd -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()
        else:
            seq_sint_tokens.append(token_atual[0])
            aux_idx_token = lista_arg(idx_token, lex_tokens, sint_tokens)
            idx_token = aux_idx_token

            print(f"cmd -- CAPTUROU TOKEN: ['cmd'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()

    elif "begin" in token_atual:
        seq_sint_tokens.append("begin")
        idx_token += 1 
        aux_idx_token = variaveis(idx_token, lex_tokens, sint_tokens)
    
        idx_token = aux_idx_token
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    return idx_token



def condicao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0

    aux_idx_token = expressao(idx_token, lex_tokens, sint_tokens)

    idx_token = aux_idx_token

    token_atual = lex_tokens[idx_token]
    expectativa = "relacao"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

        idx_token += 1
        aux_idx_token = expressao(idx_token, lex_tokens, sint_tokens)

        idx_token = aux_idx_token

        print(f"cmd -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "condicao"])
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"lista_par -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    return idx_token


def expressao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0

    aux_idx_token = termo(idx_token, lex_tokens, sint_tokens)

    idx_token = aux_idx_token
    aux_idx_token = outros_termos(idx_token, lex_tokens, sint_tokens)
    idx_token = aux_idx_token
    token_atual = lex_tokens[idx_token]

    # print(f"cmd -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
    print(f"expressao -- CAPTUROU TOKEN: ['expressao'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
    sint_tokens.append([seq_sint_tokens, "expressao"])
    # seq_sint_tokens.clear()

    return idx_token


def outros_termos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    if '+' or '-' in token_atual:
        aux_idx_token = op_ad(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        aux_idx_token = termo(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        aux_idx_token = outros_termos(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token
        print(f"outros_termos -- CAPTUROU TOKEN: ['expressao'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append(seq_sint_tokens, "outros_termos")

    else:
        seq_sint_tokens.append("outros_termos")
        print(f"outros_termos -- CAPTUROU TOKEN: ['outros_termos'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        
    return idx_token


    
def op_ad(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "+"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"op_ad -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "op_ad"])
        # seq_sint_tokens.clear()
    elif "-" in token_atual:
        seq_sint_tokens.append("-")
        print(f"op_ad -- CAPTUROU TOKEN: ['{expectativa}'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "op_ad"]) 
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"op_ad -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    return idx_token



def termo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    aux_idx_token = 0

    token_atual = lex_tokens[idx_token]
    expectativa = "op_un"
    if expectativa in token_atual:
        idx_token += 1
        aux_idx_token = fator(idx_token, lex_tokens, sint_tokens)

        idx_token = aux_idx_token
        aux_idx_token = mais_fatores(idx_token, lex_tokens, sint_tokens)

        idx_token = aux_idx_token

        token_atual = lex_tokens[idx_token]
        print(f"termo -- CAPTUROU TOKEN: ['termo'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "termo"])
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual, expectativa])
        print(f"termo -- Erro na comparacao: ['{expectativa}'] com o token {token_atual} - Idx: [{idx_token}]")

    return idx_token



def mais_fatores(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    aux_idx_token = 0

    token_atual = lex_tokens[idx_token]
    expectativa = "op_mul"
    if expectativa in token_atual:
        idx_token += 1
        aux_idx_token = fator(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        aux_idx_token = mais_fatores(idx_token, lex_tokens, sint_tokens)

        token_atual = lex_tokens[idx_token]
        idx_token = aux_idx_token
        print(f"mais_fatores -- CAPTUROU TOKEN: ['mais_fatores'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append(seq_sint_tokens, "mais_fatores")
 
    else:
        seq_sint_tokens.append("mais_fatores")
        sint_tokens.append(seq_sint_tokens, "mais_fatores")
        print(f"mais_fatores -- CAPTUROU TOKEN: ['mais_fatores'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")

    return idx_token



def fator(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"fator -- CAPTUROU TOKEN: ['fator'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "fator"])
        # seq_sint_tokens.clear()
    elif "numero_int" in token_atual:
        seq_sint_tokens.append("numero_int")
        print(f"fator -- CAPTUROU TOKEN: ['fator'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "fator"])
        # seq_sint_tokens.clear()
    elif "numero_real" in token_atual:
        seq_sint_tokens.append("numero_real")
        print(f"fator -- CAPTUROU TOKEN: ['fator'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "fator"])
        # seq_sint_tokens.clear()
    elif "(" in token_atual:
        seq_sint_tokens.append(token_atual[0])

        idx_token += 1 
        aux_idx_token = expressao(idx_token, lex_tokens, sint_tokens)
        idx_token = aux_idx_token

        print(f"fator -- CAPTUROU TOKEN: ['fator'] com o token {token_atual} - Sequencia: {seq_sint_tokens} - Idx: [{idx_token}]")
        sint_tokens.append([seq_sint_tokens, "fator"])

    return idx_token


###########################################################################################################

def print_sint_tokens(sint_tokens):
    print("\n----------Tokens----------")
    
    cont_sint_tokens = len(sint_tokens)
    print("\nTotal de sint_tokens: " + str(cont_sint_tokens))
    if cont_sint_tokens > 0:
        for i in range(cont_sint_tokens):
                print("Token[" + str(i) + "]: " + str(sint_tokens[i]))
        
    print("\n")
