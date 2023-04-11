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
    global lexi_tokens, res_words
    
    dc(idx_token, sint_tokens)
    
    token_atual = lexi_tokens[idx_token]
    
    if "simb_ponto" in token_atual:
        idx_token += 1
        token_atual = lexi_tokens[idx_token]

        # pegar chave de dicionario
        key_list = list(res_words.keys())
        val_list = list(res_words.values())
        begin = val_list.index("begin")

        if "begin" in token_atual:
            idx_token += 1
            token_atual = lexi_tokens[idx_token]

            # comandos(idx_token, sint_tokens)

            idx_token += 1
            token_atual = lexi_tokens[idx_token]
            if "end" in token_atual:
                sint_tokens.append([token_atual, "corpo"])
            
            else:
                print(f"corpo -- erro no {token_atual}")
        else:
            print(f"corpo -- erro no {token_atual}")
    else:
        print(f"corpo -- erro no {token_atual}")
                            

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

def variaveis(idx_token, sint_tokens):
    global lexi_tokens
    
    token_atual = lexi_tokens[idx_token]
    if "ident" in token_atual:
        idx_token += 1
        mais_var(idx_token, sint_tokens)
        sint_tokens.append([token_atual, "variaveis"])
    else:
        print(f"variaveis -- erro no {token_atual}")

            


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