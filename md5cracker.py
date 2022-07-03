from colorama import Fore, Back, Style
import colorama
import hashlib
import sys


def md5crack(hash_file, wordlists):
    HASHES = []
    check = []
    try:
        hashdocument = open(hash_file, 'r')
    except IOError:
        print("Hash file not Found!")
        sys.exit()
    else:
        crack = hashdocument.readlines()
        
        print(f'\n[*] cracking {len(crack)} hashe(s)')

        for HASH in crack:
            crack = HASH.strip() # striping the hashes from the newlines
            HASHES.append(crack)

        for crack in HASHES:
            print(f'\ncracking: {crack}')
            try:
                wordlistfile = open(wordlists, 'r', encoding='latin1').readlines()
            except IOError:
                print("Wordlist file not found!")
                sys.exit()
            else:
                for line in wordlistfile: # Reading through the wordlist.
                    line = line.strip() # removing any new lines character
                    md5crack = hashlib.md5(line.encode())  # calling the algorithm type we want to crack
                    word_hash = md5crack.hexdigest() # Updates the hash input by the words in the wordlist using 'utf-8' encoding
                    if word_hash == crack: # Checking if the word_hash equal to the hash 
                        # print(Fore.BLUE + f"\n[*] Great! The word match to the given hash is: {Fore.GREEN + line}")
                        print(f'cracked: {line}')
                        check.append('1')
                    if len(check) == len(HASHES):
                        exit('\n[*] Done ;)')
                        
                

if __name__ == '__main__':      
    try:
        print(Fore.LIGHTMAGENTA_EX +"MD5 Crack\n")
        print(Fore.GREEN + "MD5 Hashes crack, store hashes & list in .txt\n")
        hash_file = input("[*] Name of Hashes File: ")
        wordlist = input("[*] Name of the Wordlist: ")
        md5crack(hash_file, wordlist)
    except KeyboardInterrupt:
        print(Fore.RED + "\nExisting ...")
        sys.exit()
