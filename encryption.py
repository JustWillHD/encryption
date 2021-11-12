alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start, cipher_dir, shifted):

  end_text = ""
  if cipher_dir == "decode":
    shifted *= -1
  for char in start:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shifted
      end_text += alphabet[new_position]
    else:
      end_text += char
    

    
  print(f"Encoded {cipher_dir}d result: {end_text}")




cont = True

while cont:
  print("Welcome to Will's encryption algorithm")
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  
  shift = shift % 26
  caesar(start=text, shifted=shift, cipher_dir=direction)

  result = input("Type 'yes' or 'no' if you want to play again. \n")
  if result == "no":
    should_continue = False
    break
