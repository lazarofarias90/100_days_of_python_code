from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('Type "encode" to encrypt, type "decode" to decryot:\n').lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):

    cipher_text = ""

    for char in original_text:

        position = alphabet.index(char)
        new_position = (position + shift_amount) % len(alphabet)
        cipher_text += alphabet[new_position]

    print(f"The encoded text is {cipher_text}")

def decrypt(original_text, shift_amount):
    
    output_text = ""

    for char in original_text:

        position = alphabet.index(char)
        new_position = (position - shift_amount) % len(alphabet)
        output_text += alphabet[new_position]

    print(f"The encoded text is {output_text}")

def ceasar(original_text, shift_amount, encode_or_decode):

    output_text = ""

    for char in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        position = alphabet.index(char)
        new_position = (position + shift_amount) % len(alphabet)
        output_text += alphabet[new_position]

    print(f"The {encode_or_decode}d text is {output_text}")

# encrypt(text, shift)
# decrypt(text, shift)   
ceasar(text, shift, direction)