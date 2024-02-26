alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			'v', 'w', 'x', 'y', 'z']



def my_encrypt (plain_text, shift):
	encrypted_word = ''
	letter_position = 0
	for letter in plain_text:
		position = 0
		for char in alphabet:
			if char == letter:
				letter_position = position
			position += 1
		encrypted_position = letter_position + shift
		if encrypted_position >= len(alphabet):
			encrypt_letter = alphabet[abs(len(alphabet)-encrypted_position)]
		else:
			encrypt_letter = alphabet[letter_position+shift]
		encrypted_word += encrypt_letter
	return print(f'This is your encrypted word: "{encrypted_word}"')

def other_encrypt (plain_text, shift_amount):
	cipher_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		new_position = position + shift_amount
		new_letter = alphabet[new_position]
		cipher_text += new_letter
	#they cheated by adding extra letters to the alphabet list
	return print(cipher_text)

def my_decrypt(plain_text,shift):
	decrypted_message = ''
	for letter in plain_text:
		position = alphabet.index(letter)
		decrypted_message += alphabet[position - shift]
	return print(decrypted_message)

def caesar(direction, text, shift, keep_going): #same as encrypt and decrypt, but combined
	message = ''
	numbers = [0,1,2,3,4,5,6,7,8,9]
	if direction == 'decode':
		shift *= -1
	for letter in text:
		if not letter.isalpha():
			message += letter
			continue
		position = alphabet.index(letter)
		# if direction == "encode":
		# 	encrypted_position = position + shift
		# 	if encrypted_position >= len(alphabet):
		# 		message += alphabet[abs(len(alphabet) - encrypted_position)]
		# 	else:
		# 		message += alphabet[encrypted_position]
		# if direction == 'decode':
		# 	message += alphabet[position - shift]
		shift = shift % 26 #int(round(((shift / 26) - int(shift/26))*26,0))
		encrypted_position = position + shift
		if encrypted_position >= len(alphabet):
			message += alphabet[abs(len(alphabet) - encrypted_position)]
		else:
			message += alphabet[encrypted_position]
	print(f'Here is your message: {message}')
	ask = str(input("Do you want to keep going? Type yes or no\n")).lower()
	if ask == "no":
		keep_going = False
	return keep_going

keep_going = True
while keep_going == True:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	keep_going = caesar(direction,text,shift, keep_going)
