import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('hello.go','r')
    for word in dictFile.readlines():
        word = word.strip(' ')
        cryptWord = crypt.crypt(word.salt)
        if(crypt == cryptPass):
            print("[+] Found Password : "+word+"\n")
            return
    print("[-] Password Not Found.\n")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.spilit(':')[1].strip(' ')
            print("[*] Cracking Password For: "+user)
            testPass(cryptPass)
if __name__ == "__main__":
    main()
        
