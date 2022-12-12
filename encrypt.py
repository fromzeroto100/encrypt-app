import pyperclip
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print("Do you want to (e)ncrypt or (d)ecrypt")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break

while True:
    maxKey = len(SYMBOLS) -1
    print("Please enter the key (0 to {}) to use".format(maxKey))
    response == input("> ").upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break



print("Enter the message to {}.".format(mode))
message = input("> ")

message = message.upper()
translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":  
  
