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

# analisador 
def get_sint_token(lex_tokens, sint_tokens):
    global total_tokens, idx_token, seq_sint_tokens

    expectativa = ""

    total_tokens = len(lex_tokens)

    token_atual = lex_tokens[idx_token]
    
    expectativa = "program"
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        seq_sint_tokens.append(expectativa)
        idx_token += 1
        token_atual = lex_tokens[idx_token]

        expectativa = "ident"
        if expectativa in token_atual:
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            seq_sint_tokens.append(expectativa)
            idx_token += 1
            token_atual = lex_tokens[idx_token]

            expectativa = ";"
            if expectativa in token_atual:
                print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                seq_sint_tokens.append(expectativa)
                idx_token += 1
                token_atual = lex_tokens[idx_token]
                corpo(idx_token, lex_tokens, sint_tokens)
                token_atual = lex_tokens[idx_token]
                
                expectativa = "simb_ponto"
                if expectativa in token_atual:
                    print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                    seq_sint_tokens.append(expectativa)
                    idx_token += 1
                    token_atual = lex_tokens[idx_token]
                    sint_tokens.append([token_atual, "programa"])

                #TODO adicionar obtencao de sint_erros                        
                else:
                    print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")
            else:
                print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")
        else:
            print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")
    else:
        print(f"get_sint_token -- Erro na comparacao {expectativa} com o token: {token_atual}")


# nao terminais
def corpo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    lex_tokens = lex_tokens

    dc(idx_token, lex_tokens, sint_tokens)
    
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    
    expectativa = "begin"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        comandos(idx_token, lex_tokens, sint_tokens)

        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "end"
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")

            sint_tokens.append([token_atual, "corpo"])
        
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    else:
        print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")

def comandos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    token_atual = lex_tokens[idx_token]

    expectativa = "cmd"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        cmd(idx_token, lex_tokens, sint_tokens) 
        
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ":    "
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            idx_token += 1 
            comandos(idx_token, lex_tokens, sint_tokens)
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    else:
        sint_tokens.append([token_atual, "comandos"])

def cmd(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
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
                print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    
    elif "write" in token_atual:
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "("
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            variaveis(idx_token, lex_tokens, sint_tokens)
        
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ")"
            if expectativa in token_atual:
                seq_sint_tokens.append(expectativa)
                print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                sint_tokens.append([token_atual, "cmd"])
            else:
                print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    
    elif "if" in token_atual:
        seq_sint_tokens.append("if")
        idx_token += 1 
        condicao(idx_token, lex_tokens, sint_tokens)
        
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "then"
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            cmd(idx_token, lex_tokens, sint_tokens)
            idx_token += 1 
            p_falsa(idx_token, lex_tokens, sint_tokens)

        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")

    elif "ident" in token_atual:
        seq_sint_tokens.append("ident")
        idx_token += 1 
        token_atual = lex_tokens[idx_token]
        expectativa = "simb_atrib"
        if expectativa in token_atual:
            seq_sint_tokens.append(expectativa)
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            expressao(idx_token, lex_tokens, sint_tokens)
            sint_tokens.append([token_atual, "cmd"])
        else:
            seq_sint_tokens.append(expectativa)
            # lista_arg(idx_token, lex_tokens, sint_tokens)
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
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            sint_tokens.append([token_atual, "cmd"])
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    else:
        print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")

def condicao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    expressao(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    # relacao(idx_token, lex_tokens, sint_tokens)
    
    idx_token+=1
    expressao(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([token_atual, "condicao"])

def expressao(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    termo(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    outros_termos(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([token_atual, "expressao"])

def termo(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    op_un(idx_token, lex_tokens, sint_tokens)
    
    idx_token+=1
    fator(idx_token, lex_tokens, sint_tokens)

    idx_token+=1
    mais_fatores(idx_token, lex_tokens, sint_tokens)

    token_atual = lex_tokens[idx_token]
    sint_tokens.append([token_atual, "termo"])

def op_un(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    token_atual = lex_tokens[idx_token]
    expectativa = "+"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_un"])
    elif "-" in token_atual:
        seq_sint_tokens.append("-")
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_un"])
    else:
        seq_sint_tokens.append("op_un")
        sint_tokens.append([token_atual, "op_un"])
    
def fator(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "fator"])
    elif "numero_int" in token_atual:
        seq_sint_tokens.append("numero_int")
        sint_tokens.append([token_atual, "fator"])
    elif "numero_real" in token_atual:
        seq_sint_tokens.append("numero_real")
        sint_tokens.append([token_atual, "fator"])
    else:
        expressao(idx_token, lex_tokens, sint_tokens)

def mais_fatores(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    op_mul(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    fator(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    mais_fatores(idx_token, lex_tokens, sint_tokens)
    #TODO ver como fazer o OR de vazio

def op_mul(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    token_atual = lex_tokens[idx_token]
    expectativa = "*"
    if expectativa in token_atual:
        seq_sint_tokens.append(expectativa)
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_mul"])
    elif "/" in token_atual:
        seq_sint_tokens.append("/")
        sint_tokens.append([token_atual, "op_mul"]) 
    else:
        print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
  
def outros_termos(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    op_ad(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    termo(idx_token, lex_tokens, sint_tokens)
    idx_token+=1

    outros_termos(idx_token, lex_tokens, sint_tokens)
    #TODO ver como fazer o OR de vazio
    
def op_ad(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    token_atual = lex_tokens[idx_token]
    expectativa = "+"
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        sint_tokens.append([token_atual, "op_ad"])
    elif "-" in token_atual:
        sint_tokens.append([token_atual, "op_ad"]) 
    else:
        print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")









#TODO reposicionar
def p_falsa(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens

    token_atual = lex_tokens[idx_token]
    expectativa = "else"
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token+=1
        cmd(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "p_falsa"])
    else:
        sint_tokens.append([token_atual, "p_falsa"])

def variaveis(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    token_atual = lex_tokens[idx_token]
    expectativa = "ident"
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        # seq_sint_tokens.append(expectativa)
        idx_token += 1
        # mais_var(idx_token, lex_tokens, sint_tokens)
        sint_tokens.append([token_atual, "variaveis"])
    else:
        print(f"variaveis -- erro no {token_atual}")
            

def dc(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    dc_v(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    dc_p(idx_token, lex_tokens, sint_tokens)
    token_atual = lex_tokens[idx_token]

    sint_tokens.append([token_atual, "dc"])

def dc_v(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    token_atual = lex_tokens[idx_token]
    expectativa = "var"
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1    
        variaveis(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ":"
        if expectativa in token_atual:
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1 
            # tipo_var(idx_token, lex_tokens, sint_tokens)
            idx_token += 1 
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                idx_token += 1 
                dc_v(idx_token, lex_tokens, sint_tokens)

            else:
                print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    else:
        sint_tokens.append([token_atual, "dc_v"])

def dc_p(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    token_atual = lex_tokens[idx_token]
    expectativa = "procedure"
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = "ident"
        if expectativa in token_atual:
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            idx_token += 1
            parametros(idx_token, lex_tokens, sint_tokens)
            idx_token += 1
            token_atual = lex_tokens[idx_token]
            expectativa = ";"
            if expectativa in token_atual:
                print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
                idx_token += 1
                # corpo_p(idx_token, lex_tokens, sint_tokens)
                idx_token += 1
                dc_p(idx_token, lex_tokens, sint_tokens)
            else:
                print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    else:
        sint_tokens.append([token_atual, "dc_p"])

def parametros(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    token_atual = lex_tokens[idx_token]
    expectativa = "("
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        lista_par(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        token_atual = lex_tokens[idx_token]
        expectativa = ")"
        if expectativa in token_atual:
            print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
            sint_tokens.append([token_atual, "parametros"])
        else:
            print(f"nome_padrao -- Erro na comparacao 'comp_padrao' com o token: {token_atual}")
    else:
        sint_tokens.append([token_atual, "parametros"])

def lista_par(idx_token, lex_tokens, sint_tokens):
    global seq_sint_tokens
    
    token_atual = lex_tokens[idx_token]
    variaveis(idx_token, lex_tokens, sint_tokens)
    idx_token += 1
    token_atual = lex_tokens[idx_token]
    expectativa = ":"
    if expectativa in token_atual:
        print(f"get_sint_token -- Sucesso na comparacao {expectativa} com o token: {token_atual}")
        idx_token += 1
        # tipo_var(idx_token, lex_tokens, sint_tokens)
        idx_token += 1
        # mais_par(idx_token, lex_tokens, sint_tokens)
        token_atual = lex_tokens[idx_token]
        sint_tokens.append([token_atual, "lista_par"])



    



#TODO   fazer um contador de tokens
#        para criar a funcao de obter simbolo

def print_sint_tokens(sint_tokens):
    print("\n----------sint_tokens----------")
    
    cont_sint_tokens = len(sint_tokens)
    print("\nTotal de sint_tokens: " + str(cont_sint_tokens))
    if cont_sint_tokens > 0:
        for i in range(cont_sint_tokens):
                print("Token[" + str(i) + "]: " + str(sint_tokens[i]))
        
    print("\n")