from ART import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                                                                # Can use the modulo function to divide the alphabet by 26.
                                                                ##instead of doubling the list function.--- Chatgpt recommendation.


print(f"""
        {logo}
        Welcome to Caesar's Cipher
        """)


def encrypt(original_text, shift_amount):
    encrypted_word = ""
    for i in original_text:
        if i in alphabet:
            pos_number = alphabet.index(i)
            encrypted_word += alphabet[pos_number + shift_amount]
        else:
            encrypted_word+= i
    print(f"The encrypted word is {encrypted_word}")



def decrypt(final_text, shift_adjustment):
    decrypted_word = ""
    for i in final_text:
        if i in alphabet:
            pos_number = alphabet.index(i)
            decrypted_word += alphabet[pos_number - shift_adjustment]
        else:
            decrypted_word+=i
    print(f" The decrypted word is: {decrypted_word}")


        # Did use chatgpt to add the spaces using if and else statements
                                                                        ## Need to think about all the different scenarios of it working out.
game_continue= True
while game_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)

    elif direction == "decode":
        decrypt(final_text= text, shift_adjustment = shift )
    else:
        print("Please choose one of the two options!")

    game_finish = input("Would you like to go again?Yes or No").lower()
    if game_finish == "no":
        game_continue = False
        print("Thanks for playing!")






