#Author: Ameer Alsalati
#Date of completion: 17/11/22
#How to use? https://github.com/theyellowray0/Caesars-cipher-with-file-handling-and-brute-force-decryption-flagship-S4-project-/tree/main

import sys
import os
class Cipher:

    @staticmethod
    def find_last_line():
        with open(os.path.join(sys.path[0], "input.txt"), "rb") as file:
           file.seek(-2, os.SEEK_END)
           while file.read(1) != b'\n':
              file.seek(-2, os.SEEK_CUR) 
           key = file.readline().decode()
        return key
    


    @staticmethod
    def key(key, counter, length, activate, here):
        activate = False
        key = key.strip()
        if key[-1] == "*" and len(key) == 2:
            key = int(key[0])
            key = str(key)
            key += "*"
            here = False

        elif key[-1] == "*" and ((int(key[0]) * 10) + (int(key[1]))) >= 1 and ((int(key[0]) * 10) + (int(key[1]))) <= 25:
            key = ((int(key[0]) * 10) + (int(key[1])))
            key = str(key)
            key += "*"
            here = False

        if here == True:
            if key[-1] != "*":
               activate = True
               if counter <= (length - 1):
                  key = key[counter]
                  counter += 1
                  
               else:
                  counter = 0
                  key = key[counter]
                  counter += 1
                  
        return key, counter, activate, here


    @staticmethod
    def encrypt(string,key, length):
        counter = 0
        activate = False
        here = True
        build_word = ""
        key = str(key)
        for char in string:
            keys, counter, activate, here = Cipher.key(key, counter, length, activate, here)
            key = key.replace('*', "")
            keys = keys.replace("*", "")
            if char == " ":
                build_word += " "
                continue
            if ord(char) > 96 :
                build_word += chr((ord(char) + int(keys) - 97) % 26 + 97)
            else:
                build_word += chr((ord(char)+ int(keys) - 65) % 26 + 65)

            if activate == True:
                pass
            else:
               key += "*"
        
        return build_word

    @staticmethod
    def decrypt(string, key, length, counters):
        if key == "x":
            counters += 1
            key = counters
            key = str(key) + "*"
            length = len(key)

        counter = 0
        activate = False
        here = True
        build_word = ""
        key = str(key)
        for char in string:
            keys, counter, activate, here = Cipher.key(key, counter, length, activate, here)
            keys = keys.replace('*', "")
            key = key.replace("*", "")
            if char == " ":
                build_word += " "
                continue
            if ord(char) > 96:
                build_word += chr((ord(char) - int(keys) - 97) % 26 + 97)
            else:
                build_word += chr((ord(char) - int(keys) -65) % 26 +65)

            if activate == True:
               pass
            else:
               key += "*"
        return build_word, counters

    @staticmethod
    def file_handle_procedure():
        ready = False
        global counter
        global input
        global text
        global key
        count = 0

        while ready == False:
            pending = input("When your file arrangment is ready, hit return.")
            ready = True
        with open(os.path.join(sys.path[0], "input.txt"), "r+") as input:
            lines_1 = len(input.readlines())
            key = Cipher.find_last_line()
            key = key.rstrip('\n')
            #text = text.strip()
            input.seek(0)
            with open(os.path.join(sys.path[0], "output.txt"),"w") as output:
               for index in range(0, lines_1 - 1):
                  last_pos = input.tell()
                  input.seek(last_pos)
                  text = input.readline()
                  text = text.rstrip('\n')
                  global encrypted
                  length = len(key)
                  encrypted = Cipher.encrypt(text,key, length)
                  print(encrypted)
                  output.write(encrypted + '\n')
            

        
    @staticmethod   
    def decrypt_file():
        ready = False
        global counter
        global input
        global key
        counters = 0
        while ready == False:
            pending = input("When your file arrangment is ready, hit return.")
            ready = True
        with open(os.path.join(sys.path[0], "input.txt"), "r+") as input:
            lines_1 = len(input.readlines())
            key = Cipher.find_last_line()
            key = key.strip()
            #text = text.strip()
            input.seek(0)
            with open(os.path.join(sys.path[0], "output.txt"),"w") as output:
                for index in range(lines_1 - 1):
                  last_pos = input.tell()
                  input.seek(last_pos)
                  text = input.readline()
                  text = text.rstrip('\n')
                  global decrypted
                  length = len(key)
                  decrypted, counters = Cipher.decrypt(text,key, length, counters)
                  output.write(decrypted + '\n')
    
    @staticmethod
    def crack():
       
        counters = 0
        key = "x"
        length = "x"
        String = input("Please enter the string you wish to crack: ")
        for index in range(26):
            decrypted, counters = Cipher.decrypt(String, key, length, counters)
            print("")
            print("Pass " + str(index + 1) + ": " + decrypted)


#----Testing-------
if __name__ == "__main__":
    ready = False
    counters = 0
    counter = 0
    desision = input("Would you like to read lines from a file, or type the phrase, or force decrypt(Y or N or F)? ")
    if desision == "Y":
        print("Please place your input text file (input.txt) into the same directroy as this program, make sure the last line is made up of the key exclusivley")
        desision_1 = input("Would you like to encrypt or decrypt a file (E or D respecitvely)? ")
        if desision_1 == "E":
            Cipher.file_handle_procedure()
            print("File succesfully processed, you may open 'output.txt'")
        else:
            key = ""
            Cipher.decrypt_file()
            print("File succesfully processed, you may open 'output.txt'")
    elif desision == "F":
        Cipher.crack()
    else:
        desision_2 = input("Would you like to encrypt or decryp (E or D)?")
        if desision_2 == 'E':

           String = input("Please enter a phrase to encrypt: ")
           key = input("Choose your key (a number of letters to shift in the alphabet), place an asterisk at the end to signify an entire integer: ")
           length = len(key)
           encrypted = Cipher.encrypt(String,key, length)
           print("Encrypted : ", encrypted)
        else:
           String = input("Please enter a phrase to decrypt: ")
           key = input("Choose your key (a number of letters to shift in the alphabet), place an asterisk at the end to signify an entire integer: ")
           length = len(key) 
           decrypted, counters = Cipher.decrypt(String, key, length, counters)
           print("Decrypted: ", decrypted)
        
        


    
