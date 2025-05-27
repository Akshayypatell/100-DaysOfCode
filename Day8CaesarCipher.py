alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
rearranged_alphabets = []
var1 = True


def encode(text):
    encode1 = ""
    for char in text:
        Index1 = alphabets.index(char)
        encode1 += rearranged_alphabets[Index1]
    print(f"Here's the encoded result {encode1}")


def decode(text):
    decode1 = ""
    for char in text:
        Index1 = rearranged_alphabets.index(char)
        decode1 += alphabets[Index1]
    print(f"Here's the encoded result {decode1}")


while var1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text1 = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    for val in range(len(alphabets)):
        if val >= shift:
            rearranged_alphabets.append(alphabets[val])
    for val in range(len(alphabets)):
        if val < shift:
            rearranged_alphabets.append(alphabets[val])

    if direction == "encode":
        decode(text1)
    elif direction == "decode":
        encode(text1)
    check = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if check == "yes":
        var1 = True
    elif check == "no":
        var1 = False
