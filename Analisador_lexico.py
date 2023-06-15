import re

def validate_input(input_str):
    
    pattern = r'^[a-wA-W0-9]{1,10}$'
    if re.match(pattern, input_str):
        print("String aceita.")

    
    math_pattern = r'[xyztw\d][+\-*/()[\]{}@#!\w\d]*(?<![\+\-\*/(){}\[\]])$'
    if re.match(math_pattern, input_str):
        print("A string é uma expressao matematica.")
    else:
        print("Não é uma expressão matematica")
    
    var_sist = r'^[0-9]'
    if re.match(var_sist, input_str):
        print("Palavra reservada pelo sistema")


user_input = input("Enter your input: ")
validate_input(user_input)
