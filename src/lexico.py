from palavras_reservadas import digit, interrompe_string, letter, reserved_words, estados            

#array que armazena os tokens
# token = []
#array que armazena os erros
lex_erro = []

#controle da maquina de estados
estado = estados
mc_state = estado["S_HEADER_STATE"]

#concatenacao de dados 
string_to_analyze = ""
number_to_analyze = 0
comment = ""

#controle de abre&fechas
coment_aberto = []
parenteses_aberto = []
begin_aberto = []

#BUG em ponto_virgula, virgula, parenteses, igual

#NOTE analisa o caractere, individualmente e como cadeia, e retorna o token
def get_lex_token(character, num_character, lex_tokens):
    global mc_state, string_to_analyze, number_to_analyze, comment
    global coment_aberto, parenteses_aberto, begin_aberto

    match(mc_state):
        #NOTE case header_state funcionando
        case "s_header_state":
            #conjuntos de caracteres
            if character in letter:
                string_to_analyze = string_to_analyze + character
                #print("eh letra, cadeia: " + string_to_analyze)
                mc_state = "s_string"
            elif character in digit:
                number_to_analyze = (number_to_analyze) + int(character)
                #print("number_to_analyze: "  + str(number_to_analyze))
                mc_state = "s_digit"
            
            #operadores relacionais
            elif character == ",":
                lex_tokens.append([character,","])
                mc_state = "s_header_state"    
            elif character == ";":
                lex_tokens.append([character,";"])
                mc_state = "s_header_state"
            elif character == "=":
                lex_tokens.append([character,"="])
                mc_state = "s_header_state"
            elif character == ".":
                lex_tokens.append([character,"."])
                mc_state = "s_header_state"    
            elif character == "<":
                mc_state = "s_menor_que"
            elif character == ">":
                mc_state = "s_maior_que"
            elif character == ":":
                mc_state = "s_dois_pontos"
            
            #operadores matematicos
            elif character == "+":
                lex_tokens.append([character, "op_ad"])
                mc_state = "s_header_state"
            elif character == "-":
                lex_tokens.append([character, "op_ad"])
                mc_state = "s_header_state" 
            elif character == "*":
                lex_tokens.append([character, "op_mul"])
                mc_state = "s_header_state"
            elif character == "/":
                lex_tokens.append([character, "op_mul"])
                mc_state = "s_header_state"

            #operador de comentario
            elif character == "{":
                coment_aberto.append(num_character)
                comment = comment + character
                mc_state = "s_abre_coment"
            
            #caracteres skipaveis
            elif character == " ":
                mc_state = "s_header_state"            
            elif character == " ":
                mc_state = "s_header_state"            
            elif character == "\t":
                mc_state = "s_header_state"
            elif character == "\n":
                mc_state = "s_header_state"            
                        
            #parenteses
            elif character == "(":
                parenteses_aberto.append(num_character)
                mc_state = "s_abre_parent"
            elif character == ")":
                parenteses_aberto.pop()
                mc_state = "s_header_state"

            #caractere irreconhecivel
            else:
                lex_erro.append(["unreconized_char", num_character, character])
                #print("ERRO: caracter irreconhecivel!, no caractere " + str(num_character)) 

        #NOTE case parenteses
        case "s_abre_parent":
            if character == ")":
                parenteses_aberto.pop()
                mc_state = "s_header_state"
            elif character in letter:
                string_to_analyze = string_to_analyze + character
                mc_state = "s_string"
            elif character in digit:    
                number_to_analyze = (number_to_analyze) + int(character)
                print("s_abre_parent/number_to_analyze: "  + str(number_to_analyze))
                mc_state = "s_digit"

        #NOTE case comentario funcionando
        case "s_abre_coment":
            if character == "}":
                comment = comment + character
                coment_aberto.pop()
                lex_tokens.append([comment,"comentario"])
                mc_state = "s_header_state"
            elif character == "\0":
                lex_erro.append(["coment_aberto", num_character, character])
                #print("ERRO: comentario aberto!, no caractere " + str(num_character))
                mc_state = "s_header_state"
            else:
                comment = comment + character
                mc_state = "s_abre_coment"

        #NOTE case de identificadores ou palavras reservadas funcionando
        case "s_string":
            if character in letter:
                string_to_analyze = string_to_analyze + character
                mc_state = "s_string"
            elif character in digit:
                string_to_analyze = string_to_analyze + character
                mc_state = "s_string"
            elif character in interrompe_string:
 
                if is_reserved(string=string_to_analyze, lex_tokens=lex_tokens):
                    pass
                
                #operadores relacionais
                elif character == ",":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character,","])
                    mc_state = "s_header_state"    
                elif character == ";":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character,";"])
                    mc_state = "s_header_state"
                elif character == "=":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character,"="])
                    mc_state = "s_header_state"
                elif character == ".":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character,"."])
                    mc_state = "s_header_state"    
                elif character == "<":
                    mc_state = "s_menor_que"
                elif character == ">":
                    mc_state = "s_maior_que"
                elif character == ":":
                    mc_state = "s_dois_pontos"
                
                #operadores matematicos
                elif character == "+":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character, "op_ad"])
                    mc_state = "s_header_state"
                elif character == "-":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character, "op_ad"])
                    mc_state = "s_header_state" 
                elif character == "*":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character, "op_mul"])
                    mc_state = "s_header_state"
                elif character == "/":
                    lex_tokens.append([string_to_analyze, "ident"])
                    lex_tokens.append([character, "op_mul"])
                    mc_state = "s_header_state"

                #operador de comentario
                elif character == "{":
                    coment_aberto.append(num_character)
                    comment = comment + character
                    mc_state = "s_abre_coment"
                
                #caracteres skipaveis
                elif character == " ":
                    lex_tokens.append([string_to_analyze, "ident"])
                    mc_state = "s_header_state"            
                elif character == " ":
                    mc_state = "s_header_state"            
                elif character == "\t":
                    mc_state = "s_header_state"
                elif character == "\n":
                    mc_state = "s_header_state"            
                            
                #parenteses
                elif character == "(":
                    lex_tokens.append([string_to_analyze, "ident"])
                    parenteses_aberto.append(num_character)
                    mc_state = "s_abre_parent"
                elif character == ")":
                    if len(parenteses_aberto):
                        parenteses_aberto.pop()
                    mc_state = "s_header_state"
                                
                else:
                    lex_tokens.append([string_to_analyze, "ident"])
                string_to_analyze = ""
                mc_state = "s_header_state"

            else:
                lex_erro.append(["unreconized_char", num_character, character])
              
            
        
        #NOTE cases de operadores relacionais funcionando
        case "s_mais_var":
            lex_tokens.append([",", "mais_var"])
            mc_state = "s_header_state"
        
        case "s_mais_ident":
            lex_tokens.append([";", ";"])
            mc_state = "s_header_state"

        case "s_dois_pontos":
            if character == "=":
                lex_tokens.append([":=","="])
                mc_state =  "s_header_state"
            else: 
                lex_tokens.append([":",":"])
                mc_state =  "s_header_state"
        case "s_menor_que":
            if character == "=":
                lex_tokens.append(["<=","<="])        
                mc_state = "s_header_state"
            elif character == ">":
                lex_tokens.append(["<>","<>"])
                mc_state = "s_header_state"
            else:
                lex_tokens.append(["<","<"])
                mc_state = "s_header_state"
        case "s_maior_que":
            if character == "=":
                lex_tokens.append([">=",">="])
                mc_state = "s_header_state"
            else:
                lex_tokens.append([">",">"])
                mc_state = "s_header_state"
        
        #NOTE cases de digitos funcionando
        case "s_digit":
            if character in digit:
                number_to_analyze = (number_to_analyze*10) + int(character)
                #print("number_to_analyze: " + str(number_to_analyze))
                mc_state = "s_digit"
            elif character == ".":
                mc_state = "s_real_numb"
            else:
                #print("number_to_analyze: " + str(number_to_analyze))
                lex_tokens.append([str(number_to_analyze),"num_inteiro"])
                number_to_analyze = 0
                mc_state = "s_header_state"
        case "s_real_numb":
            if character in digit:
                number_to_analyze = number_to_analyze + (int(character)/10)
                #print("number_to_analyze: " + str(number_to_analyze))
                mc_state = "s_real_numb2"
            else:
                lex_erro.append(["malformed_real",num_character, character])
                #print("ERRO: Num real mal formado, no caractere " + str(num_character))
        case "s_real_numb2":
            if character in digit:
                number_to_analyze = number_to_analyze + (int(character)/10)
                #print("number_to_analyze: " + str(number_to_analyze))
                mc_state = "s_real_numb2"
            else:
                lex_tokens.append([str(number_to_analyze),"num_real"])
                number_to_analyze = 0
                mc_state = "s_header_state"

#NOTE verifica se a palavra detectada eh reservada 
def is_reserved(string, lex_tokens):
    if string in reserved_words:
        #print("encontrada palavra reservada! palavra: " + string + " com token: " + reserved_words[string])
        lex_tokens.append([string, reserved_words[string]])
        return True
    else:
        return False

#NOTE mostra os lex_tokens
def print_lex_tokens(lex_tokens):
    print("\n----------lex_tokens----------")
    
    cont_lex_tokens = len(lex_tokens)
    print("\nTotal de lex_tokens: " + str(cont_lex_tokens))
    if cont_lex_tokens > 0:
        for i in range(cont_lex_tokens):
            print("Token[" + str(i) + "]: " + str(lex_tokens[i]))
    
    print("\n")

