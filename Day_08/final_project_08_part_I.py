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

encrypt(text, shift)        