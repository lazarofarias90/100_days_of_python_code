from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(original_text, shift_amount, encode_or_decode):

    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text:

        if char not in alphabet:
            output_text += char
        else:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        
    print(f"The {encode_or_decode}d text is {output_text}")
   
should_continue = True

while should_continue:

    direction = input('Type "encode" to encrypt, type "decode" to decryot:\n').lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(text, shift, direction)

    restart = input('Type "yes" if you want to go again. Otherwise, type "no".\n').lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")