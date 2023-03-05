list_num_1 = [num for num in range(97,123)] 
list_num_2 = [num for num in range(65,91)]
list_alphabet_lower = [chr(i) for i in range(97,123)]
list_alphabet_upper = [chr(j) for j in range(65,91)]

alphabet_list = list_alphabet_lower + list_alphabet_upper
num_list = list_num_1 + list_num_2

lower_alphabet = dict(zip(list_num_1, list_alphabet_lower))
upper_alphabet = dict(zip(list_num_2, list_alphabet_upper))

def rotate(character):
    if character in list_alphabet_lower:
        check_bound = ord(character) + 13
        if check_bound > 122:
            difference = check_bound - 122
            result = lower_alphabet[96+difference]
        else:
            result = lower_alphabet[check_bound]
    elif character in list_alphabet_upper:
        check_bound = ord(character) + 13
        if check_bound > 90:
            difference = check_bound - 90
            result = upper_alphabet[64+difference]
        else:
            result = upper_alphabet[check_bound]
    else:
        result = character
    return result
    
def derotate(character):
    if character in list_alphabet_lower:
        check_bound = ord(character) - 13
        if check_bound < 97:
            difference = 97 - check_bound
            result = lower_alphabet[123 - difference]
        else:
            result = lower_alphabet[check_bound]
    elif character in list_alphabet_upper:
        check_bound = ord(character) - 13
        if check_bound < 65:
            difference = 65 - check_bound
            result = upper_alphabet[91 - difference]
        else:
            result = upper_alphabet[check_bound]
    else:
        result = character
    return result
            
while True:
    message = input("Enter your message: ")
    option = input("\nEncrypt [E] / Decrypt [D]: ")

    if(option == "E"):
        encrypted_message = ""
        for character in message:
            if character in alphabet_list:
                encrypted_message += rotate(character)
            else:
                encrypted_message += character
        print(f"Encrypted message: {encrypted_message}")
      
    else:
        decrypted_message = ""
        for character in message:
            if character in alphabet_list:
                decrypted_message += derotate(character)
            else:
                decrypted_message += character
        print(f"Decrypted message: {decrypted_message}")
