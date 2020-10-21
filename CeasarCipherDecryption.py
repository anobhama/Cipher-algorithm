message="fghi"
key=5
def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    print("decrypted text is ",result)
print ("Text : " + message )
print ("Shift : " + str(key))
decrypt(key,message)