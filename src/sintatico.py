# nao-terminais sao funcoes e terminais sao ifs

# libs
from compilador import lex_tokens, sint_tokens 
from lexico import reserved_words

# globais
total_tokens = 0
idx_token = 0

sintat_tokens = sint_tokens
lexi_tokens = lex_tokens

sint_erro = []

res_words = reserved_words
# analisador 
def get_sint_token(lex_tokens, sint_tokens):
    global total_tokens, idx_token, lexi_tokens

    total_tokens = len(lex_tokens)

    token_atual = lexi_tokens[idx_token]
    
    if "programa" in token_atual:
        idx_token += 1
        token_atual = lexi_tokens[idx_token]

        if "ident" in token_atual:
            idx_token += 1
            token_atual = lexi_tokens[idx_token]

            if "mais_ident" in token_atual:
                idx_token += 1
                token_atual = lexi_tokens[idx_token]
                corpo(idx_token, sint_tokens)
                token_atual = lexi_tokens[idx_token]
               
                if "simb_ponto" in token_atual:
                    idx_token += 1
                    token_atual = lexi_tokens[idx_token]
                    sint_tokens.append([token_atual, "programa"])

 #TODO adicionar obtencao de sint_erros                        
            else:
                print(f"get_sint_token -- ja comecou errado no {token_atual}")
        else:
            print(f"get_sint_token -- ja comecou errado no {token_atual}")
    else:
        print(f"get_sint_token -- ja comecou errado no {token_atual}")
    print(sint_tokens)


# nao terminais
def corpo(idx_token, sint_tokens):
    global lexi_tokens
    
    dc(idx_token, sint_tokens)
    
    idx_token += 1
    token_atual = lexi_tokens[idx_token]
    if "begin" in token_atual:
        idx_token += 1
        comandos(idx_token, sint_tokens)

        idx_token += 1
        token_atual = lexi_tokens[idx_token]
        if "end" in token_atual:
            sint_tokens.append([token_atual, "corpo"])
        
        else:
            print(f"corpo -- erro no {token_atual}")
    else:
        print(f"corpo -- erro no {token_atual}")

def comandos(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]

    if "" in token_atual: #TODO teste
        cmd(idx_token, sint_tokens) 
        
        idx_token += 1
        token_atual = lexi_tokens[idx_token]
        if ":" in token_atual:
            idx_token += 1 
            comandos(idx_token, sint_tokens)
        else:
            print(f"comandos -- erro no {token_atual}")
    else:
        sint_tokens.append([token_atual, "comandos"])

def cmd(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    if "read" in token_atual:
        idx_token += 1 
        token_atual = lexi_tokens[idx_token]
        if "(" in token_atual:
            idx_token += 1 
            variaveis(idx_token, sint_tokens)
        
            idx_token += 1 
            token_atual = lexi_tokens[idx_token]
            if ")" in token_atual:
                sint_tokens.append([token_atual, "cmd"])
            else:
                print(f"cmd -- erro no {token_atual}")
        else:
            print(f"cmd -- erro no {token_atual}")
    
    elif "write" in token_atual:
        idx_token += 1 
        token_atual = lexi_tokens[idx_token]
        if "(" in token_atual:
            idx_token += 1 
            variaveis(idx_token, sint_tokens)
        
            idx_token += 1 
            token_atual = lexi_tokens[idx_token]
            if ")" in token_atual:
                sint_tokens.append([token_atual, "cmd"])
            else:
                print(f"cmd -- erro no {token_atual}")
        else:
            print(f"cmd -- erro no {token_atual}")
    
    elif "if" in token_atual:
        idx_token += 1 
        condicao(idx_token, sint_tokens)
        
        idx_token += 1 
        token_atual = lexi_tokens[idx_token]
        if "then" in token_atual:
            idx_token += 1 
            cmd(idx_token, sint_tokens)
            idx_token += 1 
            p_falsa(idx_token, sint_tokens)

        else:
            print(f"cmd -- erro no {token_atual}")

    elif "ident" in token_atual:
        idx_token += 1 
        token_atual = lexi_tokens[idx_token]
        if "simb_atrib" in token_atual:
            idx_token += 1 
            expressao(idx_token, sint_tokens)
            sint_tokens.append([token_atual, "cmd"])
        else:
            lista_arg(idx_token, sint_tokens)
            sint_tokens.append([token_atual, "cmd"])

    elif "begin" in token_atual:
        idx_token += 1 
        variaveis(idx_token, sint_tokens)
    
        idx_token += 1 
        token_atual = lexi_tokens[idx_token]
        if "end" in token_atual:
            sint_tokens.append([token_atual, "cmd"])
        else:
            print(f"cmd -- erro no {token_atual}")

    else:
        print(f"cmd -- erro no {token_atual}")

def condicao(idx_token, sint_tokens):
    global lexi_tokens

    expressao(idx_token, sint_tokens)

    idx_token+=1
    relacao(idx_token, sint_tokens)
    
    idx_token+=1
    expressao(idx_token, sint_tokens)

    token_atual = lexi_tokens[idx_token]
    sint_tokens.append([token_atual, "condicao"])

def expressao(idx_token, sint_tokens):
    global lexi_tokens

    termo(idx_token, sint_tokens)

    idx_token+=1
    outros_termos(idx_token, sint_tokens)

    token_atual = lexi_tokens[idx_token]
    sint_tokens.append([token_atual, "expressao"])

def termo(idx_token, sint_tokens):
    global lexi_tokens

    op_un(idx_token, sint_tokens)
    
    idx_token+=1
    fator(idx_token, sint_tokens)

    idx_token+=1
    mais_fatores(idx_token, sint_tokens)

    token_atual = lexi_tokens[idx_token]
    sint_tokens.append([token_atual, "termo"])

def op_un(idx_token, sint_tokens):
    global lexi_tokens

    token_atual = lexi_tokens[idx_token]
    if "+" in token_atual:
        sint_tokens.append([token_atual, "op_un"])
    elif "-" in token_atual:
        sint_tokens.append([token_atual, "op_un"])
    else:
        sint_tokens.append([token_atual, "op_un"])
    
def fator(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    if "ident" in token_atual:
        sint_tokens.append([token_atual, "fator"])
    elif "numero_int" in token_atual:
        sint_tokens.append([token_atual, "fator"])
    elif "numero_real" in token_atual:
        sint_tokens.append([token_atual, "fator"])
    else:
        expressao(idx_token, sint_tokens)

def mais_fatores(idx_token, sint_tokens):
    global lexi_tokens
    
    op_mul(idx_token, sint_tokens)
    idx_token+=1

    fator(idx_token, sint_tokens)
    idx_token+=1

    mais_fatores(idx_token, sint_tokens)
    #TODO ver como fazer o OR de vazio

def op_mul(idx_token, sint_tokens):
    global lexi_tokens

    token_atual = lexi_tokens[idx_token]
    if "*" in token_atual:
        sint_tokens.append([token_atual, "op_mul"])
    elif "/" in token_atual:
        sint_tokens.append([token_atual, "op_mul"]) 
    else:
        print(f"op_mul -- erro no {token_atual}")
  
def outros_termos(idx_token, sint_tokens):
    global lexi_tokens
    
    op_ad(idx_token, sint_tokens)
    idx_token+=1

    termo(idx_token, sint_tokens)
    idx_token+=1

    outros_termos(idx_token, sint_tokens)
    #TODO ver como fazer o OR de vazio
    
def op_ad(idx_token, sint_tokens):
    global lexi_tokens

    token_atual = lexi_tokens[idx_token]
    if "+" in token_atual:
        sint_tokens.append([token_atual, "op_ad"])
    elif "-" in token_atual:
        sint_tokens.append([token_atual, "op_ad"]) 
    else:
        print(f"op_ad -- erro no {token_atual}")









#TODO reposicionar
def p_falsa(idx_token, sint_tokens):
    global lexi_tokens

    token_atual = lexi_tokens[idx_token]
    if "else" in token_atual:
        idx_token+=1
        cmd(idx_token, sint_tokens)
        sint_tokens.append([token_atual, "p_falsa"])
    else:
        sint_tokens.append([token_atual, "p_falsa"])

def variaveis(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    if "ident" in token_atual:
        idx_token += 1
        mais_var(idx_token, sint_tokens)
        sint_tokens.append([token_atual, "variaveis"])
    else:
        print(f"variaveis -- erro no {token_atual}")
            

def dc(idx_token, sint_tokens):
    global lexi_tokens
    
    dc_v(idx_token, sint_tokens)
    idx_token += 1
    dc_p(idx_token, sint_tokens)
    token_atual = lexi_tokens[idx_token]

    sint_tokens.append([token_atual, "dc"])

def dc_v(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    if "var" in token_atual:
        idx_token += 1    
        variaveis(idx_token, sint_tokens)
        idx_token += 1
        token_atual = lexi_tokens[idx_token]
        if ":" in token_atual:
            idx_token += 1 
            tipo_var(idx_token, sint_tokens)
            idx_token += 1 
            token_atual = lexi_tokens[idx_token]
            if ";" in token_atual:
                idx_token += 1 
                dc_v(idx_token, sint_tokens)
            
            else:
                print(f"dc_v -- erro no {token_atual}")
        else:
            print(f"dc_v -- erro no {token_atual}")
    else:
        sint_tokens.append([token_atual, "dc_v"])

def dc_p(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    if "procedure" in token_atual:
        idx_token += 1
        token_atual = lexi_tokens[idx_token]
        if "ident" in token_atual:
            idx_token += 1
            parametros(idx_token, sint_tokens)
            idx_token += 1
            token_atual = lexi_tokens[idx_token]
            if ";" in token_atual:
                idx_token += 1
                corpo_p(idx_token, sint_tokens)
                idx_token += 1
                dc_p(idx_token, sint_tokens)
            else:
                print(f"dc_p -- erro no {token_atual}")
        else:
            print(f"dc_p -- erro no {token_atual}")
    else:
        sint_tokens.append([token_atual, "dc_p"])

def parametros(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    if "(" in token_atual:
        idx_token += 1
        lista_par(idx_token, sint_tokens)
        idx_token += 1
        token_atual = lexi_tokens[idx_token]
        if ")" in token_atual:
            sint_tokens.append([token_atual, "parametros"])
        else:
            print(f"parametros -- erro no {token_atual}")
    else:
        sint_tokens.append([token_atual, "parametros"])

def lista_par(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    variaveis(idx_token, sint_tokens)
    idx_token += 1
    token_atual = lexi_tokens[idx_token]
    if ":" in token_atual:
        idx_token += 1
        tipo_var(idx_token, sint_tokens)
        idx_token += 1
        mais_par(idx_token, sint_tokens)
        token_atual = lexi_tokens[idx_token]
        sint_tokens.append([token_atual, "lista_par"])


    



#TODO   fazer um contador de tokens
#        para criar a funcao de obter simbolo