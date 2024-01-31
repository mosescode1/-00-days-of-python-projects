# encoding text encrypting
alpha = ['a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "0", "p", "q", "r",  "s", "t", "u", "v", "w", "x", "y", "z",'a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "0", "p", "q", "r",  "s", "t", "u", "v", "w", "x", "y", "z"]

try: 
    word = input("Enter text you wan to encrypt: ").lower()
    shift = int(input("Enter the number of shift: "))
    for char in word:
        char_index = alpha.index(char)
        print(alpha[char_index + shift])
except ValueError:
     print("enter a name")
except NameError:
    print("enter ae")    

    