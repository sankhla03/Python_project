import random
import string
# # # letter_to_symbol = {
# # #     'a': '@', 'b': '!', 'c': '#', 'd': '$', 'e': '%', 
# # #     'f': '^', 'g': '&', 'h': '*', 'i': '(', 'j': ')',
# # #     'k': '-', 'l': '+', 'm': '=', 'n': '{', 'o': '}',
# # #     'p': '[', 'q': ']', 'r': ':', 's': ';', 't': '<',
# # #     'u': '>', 'v': '?', 'w': '/', 'x': '\\', 'y': '|', 'z': '~',
# # #     # For uppercase letters, you can define similar mappings
# # #     'A': '@', 'B': '!', 'C': '#', 'D': '$', 'E': '%', 
# # #     'F': '^', 'G': '&', 'H': '*', 'I': '(', 'J': ')',
# # #     'K': '-', 'L': '+', 'M': '=', 'N': '{', 'O': '}',
# # #     'P': '[', 'Q': ']', 'R': ':', 'S': ';', 'T': '<',
# # #     'U': '>', 'V': '?', 'W': '/', 'X': '\\', 'Y': '|', 'Z': '~'
# # # }


a =input("Enter your Msg: ")
wt = a.split(" ")
choice =int(input(''' Enter choice :
                  1. Encoder
                  2. Decoder '''))

if(choice==1):
  
   newword = []
   for words in wt:
      if(len(words)>=3):
        
         all_chars = string.ascii_lowercase +  string.ascii_uppercase + string.digits +string.punctuation
         r1 = ''.join(random.choices(all_chars, k=3 ))
         r2 = ''.join(random.choices(all_chars, k=3 ))
        #  r1 = "abk"
        #  r2= "ckg"
        #  s = ''.join([letter_to_symbol.get(char, char) for char in words])
         st = r1+ words[1:]+ words[0]+r2
         
         newword.append(st)
        
      else:
        #  s = ''.join([letter_to_symbol.get(char, char) for char in words])
         newword.append(words[ ::-1])

   print("".join(newword))

elif(choice==2):
   st =[]
   for w in wt:
      
      if(len(w)>=3):
         b= w[3:-3]
         a = b[-1]+b[:-1]
         st.append(a)

      else:
         st.append(w[ ::-1])

   print(" ".join(st))

else:
    print("Invalid choice!")
