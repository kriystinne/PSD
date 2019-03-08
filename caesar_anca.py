# CAESAR CODE to encrypt and decrypt messages

# original text to encrypt: Version Control System is fun

import string

a = list(string.punctuation)
a.append(" ")

txt = "Version Control System is fun!"

def encrypt(text, n):
	"""encrypt the text with a shift pattern of n"""
	encrypted = ""
	# transform each character with the ord() function into an integer and always be a letter
	# for this we need to subtract 65 from the capital letters, add the shift, take modulo and add back 65
	# CAPITAL letters start from ord("A") = 65
	# lower letters start from ord("a") = 97
	# treat punctuation differently
	for i in range(len(text)):
		if text[i].isupper():
			encrypted += chr((ord(text[i]) - 65 + n) %26 + 65)
		elif text[i] in a:
			encrypted += chr((ord(text[i]) +4))
		else:
			encrypted += chr((ord(text[i]) - 97 - n) %26 + 97)
	return encrypted


def decrypt(text, n):
	""" decrypt a text """
	decrypted = ""
	for i in range(len(text)):
		if text[i].isupper():
			decrypted += chr((ord(text[i]) -65 -n) %26 + 65)
		elif text[i] in a:
			decrypted += chr((ord(text[i]) -4))
		else:
			decrypted += chr((ord(text[i]) -97 + n)  %26 +97)
	return decrypted

if __name__ == "__main__":
	enc = encrypt(txt, 4)
	print(enc)
	print(decrypt(enc, 4))



