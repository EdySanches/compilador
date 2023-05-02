#LEXICO
interrompe_string = [" ", "\n", ":", ";", ",", "(", ")", "+", "-", "*", "/", "<", ">", "="]
digit = ['1','2','3', '4', '5', '6', '7', '8', '9', '0']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reserved_words = {"read": "read", "write": "write",
                "program": "program",
                "begin": "begin", "end": "end",
                "real": "tipo_var", "integer": "tipo_var",
                "if": "if", "then": "then", "else": "else",
                "while": "while", "do": "do",
                "var": "var"
                }

estados = {
    "S_HEADER_STATE": "s_header_state"


}