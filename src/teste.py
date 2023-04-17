from palavras_reservadas import digit, interrompe_string, letter, reserved_words, estados            
estado = estados
mc_state = estado["S_HEADER_STATE"]

print(mc_state)

import inspect

def funcao():
    return 1
def get_function_name():
    # get the frame object of the function
    frame = inspect.currentframe()
    return frame.f_code.co_name
# printing function name
print("The name of function is : " + get_function_name()) # test_function
