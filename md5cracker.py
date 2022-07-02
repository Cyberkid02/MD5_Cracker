from colorama import Fore, Back, Style
import colorama
import hashlib
import sys


def md5crack(hash_file, wordlists):
   
    try:
        hashdocument = open(hash_file, 'r')
    except IOError:
        print("Hash file not Found!")
        sys.exit()
    else:
        crack = hashdocument.readline()
        crack = crack.replace('\n', (""))

        try:
            wordlistfile = open(wordlists, 'r')
        except IOError:
            print("Wordlist file not found!")
            sys.exit()
        else:
            for line in wordlistfile: # Reading through the wordlist.
                md5crack = hashlib.md5()  # calling the algorithm type we want to crack
                line = line.replace("\n", ("")) # removing any new lines character
                md5crack.update(line.encode('utf-8')) # Updates the hash input by the words in the wordlist using 'utf-8' encoding
                word_hash = md5crack.hexdigest() # convert the word to md5 hash
                if word_hash == crack: # Checking if the word_hash equal to the hash 
                    print(Fore.BLUE + f"\n[*] Great! The word match to the given hash is: {Fore.GREEN + line}")
                    
                else:
                    pass
                

if __name__ == '__main__':      
    try:
        print(Fore.LIGHTMAGENTA_EX +"MD5 Crack\n")
        print(Fore.GREEN + "MD5 Hashes crack, store hashes & list in .txt\n")
        hash_file = input("[*] Name of Hashes File: ")
        wordlists = input("[*] Name of the Wordlist: ")
        md5crack(hash_file, wordlists)
    except KeyboardInterrupt:
        print(Fore.RED + "\nExisting ...")
        sys.exit()
