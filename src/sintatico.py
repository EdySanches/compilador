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
    global total_tokens, idx_token, seq_sint_tokens, sint_erro

    expectativa = ""

    total_tokens = len(lex_tokens)

    token_atual = lex_tokens[idx_token]
    
    expectativa = "program"
    if expectativa in token_atual:
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        seq_sint_tokens.append(expectativa)
        idx_token += 1
        token_atual = lex_tokens[idx_token]

        expectativa = "ident"
        if expectativa in token_atual:
            # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            seq_sint_tokens.append(expectativa)
            idx_token += 1
            token_atual = lex_tokens[idx_token]

            expectativa = ";"
            if expectativa in token_atual:
                # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                seq_sint_tokens.append(expectativa)
                idx_token += 1
                token_atual = lex_tokens[idx_token]
                corpo(idx_token, lex_tokens, sint_tokens)
                token_atual = lex_tokens[idx_token]
                
                expectativa = "."
                if expectativa in token_atual:
                    # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                    seq_sint_tokens.append(expectativa)
                    idx_token += 1
                    token_atual = lex_tokens[idx_token]
                    sint_tokens.append([token_atual, "programa"])

                #TODO adicionar obtencao de sint_erros                        
                #TODO adicionar obtencao do corpo de token
                else:
                    sint_erro.append(["token_inesperado", idx_token, token_atual])
                    print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")

def corpo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    lex_tokens = lex_tokens

    dc(idx_token, lex_tokens, sint_tokens)
    
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    
    expectativa = "begin"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        # print(f"corpo -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        comandos(idx_token, lex_tokens, sint_tokens)

        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            # print(f"corpo -- Sucesso na comparacao {expectativa} com o token: {token_atual}")

            sint_tokens.append([token_atual, "corpo"])
        
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"corpo -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"corpo -- Erro na comparacao {expectativa} com o token: {token_atual}")

def dc(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    dc_v(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    dc_p(idx_token, lex_tokens, sint_tokens)
    token_atual = lex_tokens[idx_token]

    sint_tokens.append([token_atual, "dc"])

def dc_v(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "var"
    if expectativa in token_atual:
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1    
        variaveis(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ":"
        if expectativa in token_atual:
            # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            tipo_var(idx_token, lex_tokens, sint_tokens)
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                idx_token += 1 
                dc_v(idx_token, lex_tokens, sint_tokens)

            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"dc_v -- Erro na comparacao {expectativa} com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"dc_v -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        sint_tokens.append([token_atual, "dc_v"])

def tipo_var(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "real"
    if expectativa in token_atual:
        # print(f"tipo_var -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "tipo_var"])

    elif "integer" in token_atual:
        # print(f"tipo_var -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "tipo_var"])

    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"tipo_var -- Erro na comparacao {expectativa} com o token: {token_atual}")

def variaveis(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        seq_sint_tokens.append(expectativa)
        idx_token += 1
        mais_var(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "variaveis"])
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"variaveis -- Erro na comparacao {expectativa} com o token: {token_atual}")

def mais_var(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = ","
    if expectativa in token_atual:
        # print(f"mais_var -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        variaveis(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "mais_var"])
    else:
        print(f"mais_var -- Erro na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "mais_var"])

def dc_p(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "procedure"
    if expectativa in token_atual:
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "ident"
        if expectativa in token_atual:
            # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1
            parametros(idx_token, lex_tokens, sint_tokens)
            idx_token += 1
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                idx_token += 1
                corpo_p(idx_token, lex_tokens, sint_tokens)
                idx_token += 1
                dc_p(idx_token, lex_tokens, sint_tokens)
                sint_tokens.append([token_atual, "dc_p"])
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"dc_p -- Erro na comparacao {expectativa} com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"dc_p -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        sint_tokens.append([token_atual, "dc_p"])

def parametros(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "("
    if expectativa in token_atual:
        # print(f"parametros -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        lista_par(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ")"
        if expectativa in token_atual:
            # print(f"parametros -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            sint_tokens.append([token_atual, "parametros"])
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"parametros -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        sint_tokens.append([token_atual, "parametros"])

def lista_par(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    variaveis(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    expectativa = ":"
    if expectativa in token_atual:
        # print(f"lista_par -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        tipo_var(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        mais_par(idx_token, lex_tokens, sint_tokens)
        token_atual = lex_tokens[idx_token]
        sint_tokens.append([token_atual, "lista_par"])
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"lista_par -- Erro na comparacao {expectativa} com o token: {token_atual}")

def mais_par(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = ";"
    if expectativa in token_atual:
        # print(f"mais_par -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        lista_par(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "mais_par"])
    else:
        # print(f"mais_par -- Erro na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "mais_par"])

def corpo_p(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    dc_loc(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    expectativa = "begin"
    if expectativa in token_atual:
        # print(f"corpo_p -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        comandos(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            # print(f"corpo_p -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                # print(f"corpo_p -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                sint_tokens.append([token_atual, "corpo_p"])

            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"corpo_p -- Erro na comparacao {expectativa} com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"corpo_p -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"corpo_p -- Erro na comparacao {expectativa} com o token: {token_atual}")

def dc_loc(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    dc_v(idx_token, lex_tokens, sint_tokens)
    
    token_atual = lex_tokens[idx_token]
    sint_tokens.append([token_atual, "lista_arg"])

def lista_arg(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(expectativa)
    
    token_atual = lex_tokens[idx_token]
    expectativa = "("
    if expectativa in token_atual:
        # print(f"lista_arg -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token+=1
        argumentos(idx_token, lex_tokens, sint_tokens)
        
        idx_token+=1
        token_atual = lex_tokens[idx_token]
        expectativa = ")"
        if expectativa in token_atual:
            # print(f"lista_arg -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            sint_tokens.append([token_atual, "lista_arg"])
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"lista_arg -- Erro na comparacao {expectativa} com o token: {token_atual}")

    else:
        sint_tokens.append([token_atual, "lista_arg"])

def argumentos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(expectativa)
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        # print(f"argumentos -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token+=1
        mais_ident(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "argumentos"])

    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"lista_arg -- Erro na comparacao {expectativa} com o token: {token_atual}")

def mais_ident(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    # seq_sint_tokens.append(expectativa)
    
    token_atual = lex_tokens[idx_token]
    expectativa = ";"
    if expectativa in token_atual:
        # print(f"lista_arg -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token+=1
        argumentos(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "mais_ident"])

    else:
        sint_tokens.append([token_atual, "mais_ident"])

def p_falsa(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "else"
    if expectativa in token_atual:
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token+=1
        cmd(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "p_falsa"])
    else:
        sint_tokens.append([token_atual, "p_falsa"])

def comandos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]

    expectativa = "cmd"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        cmd(idx_token, lex_tokens, sint_tokens) 
        
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ":    "
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            idx_token += 1 
            comandos(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([token_atual, "comandos"])
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"comandos -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        sint_tokens.append([token_atual, "comandos"])

def cmd(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]

    expectativa = "read"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "("
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            idx_token += 1 
            variaveis(idx_token, lex_tokens, sint_tokens)
        
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ")"
            if expectativa in token_atual:
                seq_sint_tokens.append(expectativa)
                sint_tokens.append([token_atual, "cmd"])
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"cmd -- Erro na comparacao {expectativa} com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"cmd -- Erro na comparacao {expectativa} com o token: {token_atual}")
    
    elif "write" in token_atual:
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "("
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            variaveis(idx_token, lex_tokens, sint_tokens)
        
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ")"
            if expectativa in token_atual:
                seq_sint_tokens.append(expectativa)
                # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                sint_tokens.append([token_atual, "cmd"])
            else:
                sint_erro.append(["token_inesperado", idx_token, token_atual])
                print(f"cmd -- Erro na comparacao {expectativa} com o token: {token_atual}")
        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"cmd -- Erro na comparacao {expectativa} com o token: {token_atual}")
    
    elif "if" in token_atual:
        seq_sint_tokens.append("if")
        idx_token += 1 
        condicao(idx_token, lex_tokens, sint_tokens)
        
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "then"
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            cmd(idx_token, lex_tokens, sint_tokens)
            idx_token += 1 
            p_falsa(idx_token, lex_tokens, sint_tokens)

        else:
            sint_erro.append(["token_inesperado", idx_token, token_atual])
            print(f"cmd -- Erro na comparacao {expectativa} com o token: {token_atual}")

    elif "ident" in token_atual:
        seq_sint_tokens.append("ident")
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = ":="
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            expressao(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([token_atual, "cmd"])
        else:
            seq_sint_tokens.append(expectativa)
            lista_arg(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([token_atual, "cmd"])

    elif "begin" in token_atual:
        seq_sint_tokens.append("begin")
        idx_token += 1 
        variaveis(idx_token, lex_tokens, sint_tokens)
    
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            sint_tokens.append([token_atual, "cmd"])
        else:
            print(f"cmd -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        print(f"cmd -- Erro na comparacao {expectativa} com o token: {token_atual}")

def condicao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    expressao(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    relacao(idx_token, lex_tokens, sint_tokens)
    
    idx_token+=1
    expressao(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([token_atual, "condicao"])

def relacao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]

    expectativa = "="
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "relacao"])

    elif "<>" in token_atual:
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "relacao"])

    elif ">=" in token_atual:
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "relacao"])

    elif "<=" in token_atual:
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "relacao"])

    elif ">" in token_atual:
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "relacao"])

    elif "<" in token_atual:
        seq_sint_tokens.append(expectativa)
        sint_tokens.append([token_atual, "relacao"])

    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"relacao -- Erro na comparacao {expectativa} com o token: {token_atual}")

def expressao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    termo(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    outros_termos(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([token_atual, "expressao"])

def op_un(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro

    token_atual = lex_tokens[idx_token]
    expectativa = "+"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_un"])
    elif "-" in token_atual:
        seq_sint_tokens.append("-")
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_un"])
    else:
        seq_sint_tokens.append("op_un")
        sint_tokens.append([token_atual, "op_un"])
    
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
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_ad"])
    elif "-" in token_atual:
        sint_tokens.append([token_atual, "op_ad"]) 
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"op_ad -- Erro na comparacao {expectativa} com o token: {token_atual}")

def termo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    op_un(idx_token, lex_tokens, sint_tokens)
    
    idx_token+=1
    fator(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    mais_fatores(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([token_atual, "termo"])

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
        seq_sint_tokens.append(expectativa)
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_mul"])
    elif "/" in token_atual:
        seq_sint_tokens.append("/")
        sint_tokens.append([token_atual, "op_mul"]) 
    else:
        sint_erro.append(["token_inesperado", idx_token, token_atual])
        print(f"nome_padrao -- Erro na comparacao {expectativa} com o token: {token_atual}")

def fator(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens, sint_erro
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        # print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "fator"])
    elif "numero_int" in token_atual:
        seq_sint_tokens.append("numero_int")
        sint_tokens.append([token_atual, "fator"])
    elif "numero_real" in token_atual:
        seq_sint_tokens.append("numero_real")
        sint_tokens.append([token_atual, "fator"])
    else:
        expressao(idx_token, lex_tokens, sint_tokens)


def print_sint_tokens(sint_tokens):
    print("\n----------sint_tokens----------")
    
    cont_sint_tokens = len(sint_tokens)
    print("\nTotal de sint_tokens: " + str(cont_sint_tokens))
    if cont_sint_tokens > 0:
        for i in range(cont_sint_tokens):
                print("Token[" + str(i) + "]: " + str(sint_tokens[i]))
        
    print("\n")