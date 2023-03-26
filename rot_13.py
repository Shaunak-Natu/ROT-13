# Create a list of ASCII codes for lowercase letters 'a' to 'z'
list_num_1 = [num for num in range(97,123)]

# Create a list of ASCII codes for uppercase letters 'A' to 'Z'
list_num_2 = [num for num in range(65,91)]

# Convert the ASCII codes for lowercase letters to actual characters using the `chr()` function
list_alphabet_lower = [chr(i) for i in range(97,123)]

# Convert the ASCII codes for uppercase letters to actual characters using the `chr()` function
list_alphabet_upper = [chr(j) for j in range(65,91)]

# Combine the lowercase and uppercase letters to create a list of all alphabets
alphabet_list = list_alphabet_lower + list_alphabet_upper

# Combine the ASCII codes for lowercase and uppercase letters to create a list of all numbers
num_list = list_num_1 + list_num_2

# Create dictionaries to map ASCII codes to corresponding lowercase and uppercase alphabets
lower_alphabet = dict(zip(list_num_1, list_alphabet_lower))
upper_alphabet = dict(zip(list_num_2, list_alphabet_upper))


# Define a function to rotate a character by 13 places
def rotate(character):
    if character in list_alphabet_lower:  # Check if character is lowercase alphabet
        check_bound = ord(character) + 13  # Get ASCII code of character and add 13
        if check_bound > 122:  # Check if the new ASCII code is beyond 'z'
            difference = check_bound - 122  # Find the difference beyond 'z'
            result = lower_alphabet[96 + difference]  # Find the corresponding rotated alphabet
        else:
            result = lower_alphabet[check_bound]  # Find the corresponding rotated alphabet
    elif character in list_alphabet_upper:  # Check if character is uppercase alphabet
        check_bound = ord(character) + 13  # Get ASCII code of character and add 13
        if check_bound > 90:  # Check if the new ASCII code is beyond 'Z'
            difference = check_bound - 90  # Find the difference beyond 'Z'
            result = upper_alphabet[64 + difference]  # Find the corresponding rotated alphabet
        else:
            result = upper_alphabet[check_bound]  # Find the corresponding rotated alphabet
    else:
        result = character  # If character is not an alphabet, don't rotate it
    return result  # Return the rotated character


def derotate(character):
    # Check if the character is a lowercase or uppercase alphabet
    if character in list_alphabet_lower:
        # Calculate the character's new ASCII value by subtracting 13
        check_bound = ord(character) - 13
        # If the new ASCII value is less than 97 (i.e., 'a'), wrap around to 'z'
        if check_bound < 97:
            difference = 97 - check_bound
            result = lower_alphabet[123 - difference]
        # Otherwise, get the character corresponding to the new ASCII value
        else:
            result = lower_alphabet[check_bound]
    elif character in list_alphabet_upper:
        # Calculate the character's new ASCII value by subtracting 13
        check_bound = ord(character) - 13
        # If the new ASCII value is less than 65 (i.e., 'A'), wrap around to 'Z'
        if check_bound < 65:
            difference = 65 - check_bound
            result = upper_alphabet[91 - difference]
        # Otherwise, get the character corresponding to the new ASCII value
        else:
            result = upper_alphabet[check_bound]
    # If the character is not an alphabet, return it as is
    else:
        result = character
    # Return the decrypted character
    return result


while True:
    # Get input from the user
    message = input("Enter your message: ")
    option = input("\nEncrypt [E] / Decrypt [D]: ")

    # If the user chooses to encrypt the message
    if (option == "E"):
        encrypted_message = ""
        # Loop through each character in the message
        for character in message:
            # If the character is an alphabet, rotate it by 13 positions
            if character in alphabet_list:
                encrypted_message += rotate(character)
            # Otherwise, add the character as is
            else:
                encrypted_message += character
        # Print the encrypted message
        print(f"Encrypted message: {encrypted_message.replace(' ', '')}")

    # If the user chooses to decrypt the message
    else:
        decrypted_message = ""
        # Loop through each character in the message
        for character in message:
            # If the character is an alphabet, derotate it by 13 positions
            if character in alphabet_list:
                decrypted_message += derotate(character)
            # Otherwise, add the character as is
            else:
                decrypted_message += character
        # Print the decrypted message
        print(f"Decrypted message: {decrypted_message}")
