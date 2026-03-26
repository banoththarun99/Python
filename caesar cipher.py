alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


    
def caeser(original_text , shifted_amount , encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shifted_amount *= -1
    for letter in original_text:
        
        if letter not in alphabet:
            output_text += letter 
        else:
        
            shifted_position = alphabet.index(letter) + shifted_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"here is the {encode_or_decode}d result : {output_text}")
    
should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
    text = input("type the message : \n").lower()
    shift = int(input("number of times the message is shifted : \n"))
       
    caeser(original_text = text , shifted_amount = shift , encode_or_decode = direction)
        
    restart = input("type 'yes' if you want to go again. otherwise , type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("goodbye")