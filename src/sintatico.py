# nao-terminais sao funcoes e terminais sao ifs

# libs
# from compilador import lex_tokens 
from palavras_reservadas import reserved_words
from inspect import currentframe
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
        print(f"get_sint_token -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        token_atual = lex_tokens[idx_token]

        expectativa = "ident"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"get_sint_token -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            idx_token += 1
            token_atual = lex_tokens[idx_token]

            expectativa = ";"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"get_sint_token -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")

                idx_token += 1
                corpo(idx_token, lex_tokens, sint_tokens)

                token_atual = lex_tokens[idx_token]
                expectativa = "."
                if expectativa in token_atual:
                    seq_sint_tokens.append(token_atual[0])
                    print(f"get_sint_token -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
                    idx_token += 1
                    token_atual = lex_tokens[idx_token]
                    sint_tokens.append([seq_sint_tokens, "programa"])
                    # seq_sint_tokens.clear()

                else:
                    sint_erro.append(["token_inesperado", idx_token, token_atual])
                    print(f"get_sint_token -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"get_sint_token -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"get_sint_token -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"get_sint_token -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def corpo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    lex_tokens = lex_tokens

    dc(idx_token, lex_tokens, sint_tokens)
    
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    
    expectativa = "begin"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"corpo -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        comandos(idx_token, lex_tokens, sint_tokens)

        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"corpo -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")

            sint_tokens.append([seq_sint_tokens, "corpo"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"corpo -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"corpo -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def dc(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    dc_v(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    dc_p(idx_token, lex_tokens, sint_tokens)

    sint_tokens.append([seq_sint_tokens, "dc"])
    # seq_sint_tokens.clear()

def dc_v(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "var"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"dc_v -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")

        idx_token += 1    
        variaveis(idx_token, lex_tokens, sint_tokens)

        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ":"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"dc_v -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            idx_token += 1 
            tipo_var(idx_token, lex_tokens, sint_tokens)
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"dc_v -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
                idx_token += 1 
                dc_v(idx_token, lex_tokens, sint_tokens)

            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"dc_v -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"dc_v -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_tokens.append([seq_sint_tokens, "dc_v"])
        # seq_sint_tokens.clear()

def tipo_var(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "real"
    if expectativa in token_atual:
        print(f"tipo_var -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        seq_sint_tokens.append(token_atual[0])
        sint_tokens.append([seq_sint_tokens, "tipo_var"])
        # seq_sint_tokens.clear()

    elif "integer" in token_atual:
        print(f"tipo_var -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        seq_sint_tokens.append("integer")
        sint_tokens.append([seq_sint_tokens, "tipo_var"])
        # seq_sint_tokens.clear()

    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"tipo_var -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def variaveis(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"variaveis -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")

        idx_token += 1
        mais_var(idx_token, lex_tokens, sint_tokens)

        sint_tokens.append([seq_sint_tokens, "variaveis"])
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"variaveis -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def mais_var(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = ","
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"mais_var -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        variaveis(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([seq_sint_tokens, "mais_var"])
        # seq_sint_tokens.clear()
    else:
        print(f"mais_var -- Sucesso na comparacao: ['null'] com o token: {token_atual}")
        sint_tokens.append([seq_sint_tokens, "mais_var"])
        # seq_sint_tokens.clear()

def dc_p(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "procedure"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"dc_p -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "ident"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"dc_p -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            idx_token += 1
            parametros(idx_token, lex_tokens, sint_tokens)
            idx_token += 1
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"dc_p -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
                idx_token += 1
                corpo_p(idx_token, lex_tokens, sint_tokens)
                idx_token += 1
                dc_p(idx_token, lex_tokens, sint_tokens)
                sint_tokens.append([seq_sint_tokens, "dc_p"])
                # seq_sint_tokens.clear()
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"dc_p -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"dc_p -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_tokens.append([seq_sint_tokens, "dc_p"])
        # seq_sint_tokens.clear()

def parametros(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "("
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"parametros -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        lista_par(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ")"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"parametros -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            sint_tokens.append([seq_sint_tokens, "parametros"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"parametros -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_tokens.append([seq_sint_tokens, "parametros"])
        # seq_sint_tokens.clear()

def lista_par(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    variaveis(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    expectativa = ":"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"lista_par -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        tipo_var(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        mais_par(idx_token, lex_tokens, sint_tokens)
        token_atual = lex_tokens[idx_token]
        sint_tokens.append([seq_sint_tokens, "lista_par"])
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"lista_par -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def mais_par(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = ";"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"mais_par -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        lista_par(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([seq_sint_tokens, "mais_par"])
        # seq_sint_tokens.clear()
    else:
        # print(f"mais_par -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
        sint_tokens.append([seq_sint_tokens, "mais_par"])
        # seq_sint_tokens.clear()

def corpo_p(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    dc_loc(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    expectativa = "begin"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"corpo_p -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token += 1
        comandos(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"corpo_p -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            idx_token += 1
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"corpo_p -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
                sint_tokens.append([seq_sint_tokens, "corpo_p"])
                # seq_sint_tokens.clear()

            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"corpo_p -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"corpo_p -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"corpo_p -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def dc_loc(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    dc_v(idx_token, lex_tokens, sint_tokens)
    
    sint_tokens.append([seq_sint_tokens, "lista_arg"])
    # seq_sint_tokens.clear()

def lista_arg(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(token_atual[0])
    
    token_atual = lex_tokens[idx_token]
    expectativa = "("
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"lista_arg -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token+=1
        argumentos(idx_token, lex_tokens, sint_tokens)
        
        idx_token+=1
        token_atual = lex_tokens[idx_token]
        expectativa = ")"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"lista_arg -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            sint_tokens.append([seq_sint_tokens, "lista_arg"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"lista_arg -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

    else:
        sint_tokens.append([seq_sint_tokens, "lista_arg"])
        # seq_sint_tokens.clear()

def argumentos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(token_atual[0])
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"argumentos -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token+=1
        mais_ident(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([seq_sint_tokens, "argumentos"])
        # seq_sint_tokens.clear()

    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"lista_arg -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def mais_ident(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(token_atual[0])
    
    token_atual = lex_tokens[idx_token]
    expectativa = ";"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"lista_arg -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token+=1
        argumentos(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([seq_sint_tokens, "mais_ident"])
        # seq_sint_tokens.clear()

    else:
        sint_tokens.append([seq_sint_tokens, "mais_ident"])
        # seq_sint_tokens.clear()

def p_falsa(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "else"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"p_falsa -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        idx_token+=1
        cmd(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([seq_sint_tokens, "p_falsa"])
        # seq_sint_tokens.clear()
    else:
        sint_tokens.append([seq_sint_tokens, "p_falsa"])
        # seq_sint_tokens.clear()

def comandos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]

    expectativa = "cmd"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"comandos -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        cmd(idx_token, lex_tokens, sint_tokens) 
        
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ":    "
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            idx_token += 1 
            comandos(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([seq_sint_tokens, "comandos"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"comandos -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_tokens.append([seq_sint_tokens, "comandos"])
        # seq_sint_tokens.clear()

def cmd(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]

    expectativa = "read"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "("
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            idx_token += 1 
            variaveis(idx_token, lex_tokens, sint_tokens)
        
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ")"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                sint_tokens.append([seq_sint_tokens, "cmd"])
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    
    elif "write" in token_atual:
        seq_sint_tokens.append("write")
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "("
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            idx_token += 1 
            variaveis(idx_token, lex_tokens, sint_tokens)
        
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ")"
            if expectativa in token_atual:
                seq_sint_tokens.append(token_atual[0])
                print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
                sint_tokens.append([seq_sint_tokens, "cmd"])
                # seq_sint_tokens.clear()
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    
    elif "if" in token_atual:
        seq_sint_tokens.append("if")
        idx_token += 1 
        condicao(idx_token, lex_tokens, sint_tokens)
        
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "then"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            idx_token += 1 
            cmd(idx_token, lex_tokens, sint_tokens)
            idx_token += 1 
            p_falsa(idx_token, lex_tokens, sint_tokens)

            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()

        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

    elif "ident" in token_atual:
        seq_sint_tokens.append("ident")
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = ":="
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            idx_token += 1 
            expressao(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()
        else:
            seq_sint_tokens.append(token_atual[0])
            lista_arg(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()

    elif "begin" in token_atual:
        seq_sint_tokens.append("begin")
        idx_token += 1 
        variaveis(idx_token, lex_tokens, sint_tokens)
    
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(token_atual[0])
            print(f"cmd -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
            sint_tokens.append([seq_sint_tokens, "cmd"])
            # seq_sint_tokens.clear()
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"cmd -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def condicao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    expressao(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    relacao(idx_token, lex_tokens, sint_tokens)
    
    idx_token+=1
    expressao(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([seq_sint_tokens, "condicao"])
    # seq_sint_tokens.clear()

def relacao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]

    expectativa = "="
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        sint_tokens.append([seq_sint_tokens, "relacao"])
        # seq_sint_tokens.clear()
    elif "<>" in token_atual:
        seq_sint_tokens.append("<>")
        sint_tokens.append([seq_sint_tokens, "relacao"])
        # seq_sint_tokens.clear()

    elif ">=" in token_atual:
        seq_sint_tokens.append(">=")
        sint_tokens.append([seq_sint_tokens, "relacao"])
        # seq_sint_tokens.clear()

    elif "<=" in token_atual:
        seq_sint_tokens.append("<=")
        sint_tokens.append([seq_sint_tokens, "relacao"])
        # seq_sint_tokens.clear()

    elif ">" in token_atual:
        seq_sint_tokens.append(">")
        sint_tokens.append([seq_sint_tokens, "relacao"])
        # seq_sint_tokens.clear()

    elif "<" in token_atual:
        seq_sint_tokens.append("<")
        sint_tokens.append([seq_sint_tokens, "relacao"])
        # seq_sint_tokens.clear()

    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"relacao -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def expressao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    termo(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    outros_termos(idx_token, lex_tokens, sint_tokens)

    sint_tokens.append([seq_sint_tokens, "expressao"])
    # seq_sint_tokens.clear()

def op_un(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "+"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"op_un -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        sint_tokens.append([seq_sint_tokens, "op_un"])
        # seq_sint_tokens.clear()
    elif "-" in token_atual:
        seq_sint_tokens.append("-")
        print(f"op_un -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        sint_tokens.append([seq_sint_tokens, "op_un"])
        # seq_sint_tokens.clear()
    else:
        seq_sint_tokens.append("op_un")
        sint_tokens.append([seq_sint_tokens, "op_un"])
        # seq_sint_tokens.clear()
    
def outros_termos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    op_ad(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    termo(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    outros_termos(idx_token, lex_tokens, sint_tokens)
    #TODO ver como fazer o OR de vazio
    
def op_ad(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "+"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"op_ad -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        sint_tokens.append([seq_sint_tokens, "op_ad"])
        # seq_sint_tokens.clear()
    elif "-" in token_atual:
        seq_sint_tokens.append("-")
        sint_tokens.append([seq_sint_tokens, "op_ad"]) 
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"op_ad -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def termo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    op_un(idx_token, lex_tokens, sint_tokens)
    
    idx_token+=1
    fator(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    mais_fatores(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([seq_sint_tokens, "termo"])
    # seq_sint_tokens.clear()

def mais_fatores(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    op_mul(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    fator(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    mais_fatores(idx_token, lex_tokens, sint_tokens)
    #TODO ver como fazer o OR de vazio

def op_mul(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "*"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"op_mul -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        sint_tokens.append([seq_sint_tokens, "op_mul"])
        # seq_sint_tokens.clear()
    elif "/" in token_atual:
        seq_sint_tokens.append("/")
        sint_tokens.append([seq_sint_tokens, "op_mul"]) 
        # seq_sint_tokens.clear()
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"op_mul -- Erro na comparacao: ['{expectativa}'] com o token: {token_atual}")

def fator(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(token_atual[0])
        print(f"fator -- Sucesso na comparacao: ['{expectativa}'] com o token: {token_atual} - Sequencia: {seq_sint_tokens}")
        sint_tokens.append([seq_sint_tokens, "fator"])
        # seq_sint_tokens.clear()
    elif "numero_int" in token_atual:
        seq_sint_tokens.append("numero_int")
        sint_tokens.append([seq_sint_tokens, "fator"])
        # seq_sint_tokens.clear()
    elif "numero_real" in token_atual:
        seq_sint_tokens.append("numero_real")
        sint_tokens.append([seq_sint_tokens, "fator"])
        # seq_sint_tokens.clear()
    else:
        expressao(idx_token, lex_tokens, sint_tokens)


def print_sint_tokens(sint_tokens):
    print("\n----------Tokens----------")
    
    cont_sint_tokens = len(sint_tokens)
    print("\nTotal de sint_tokens: " + str(cont_sint_tokens))
    if cont_sint_tokens > 0:
        for i in range(cont_sint_tokens):
                print("Token[" + str(i) + "]: " + str(sint_tokens[i]))
        
    print("\n")