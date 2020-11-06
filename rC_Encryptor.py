import os

F = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     '1','2','3','4','5','6','7','8','9','0',
     '!','?','.',',',' ','"',"'",':','_','<','>','ç','Á','á','´','`','=','/','#','$','%','&','(',')','  ','\n','-','»','»','|','+','\xa0','[',']','{','}',
     'ã','Ã','ó','Ó','é','É','À','à','*','º','&','\\','ú','Ú','ê','Ê','õ','ô','Ô','@','ª','í','Í','í']


DefaultKey = 138
N = DefaultKey
newKey = input("Key To Decrypt/Encrypt With (Press enter for Default): ")
if newKey != "" or newKey !=" ":
        try:
                N = float(newKey)
                print("Encrypting/Decrypting with key: " + str(N))
        except:
                print("Proceeding with Default Key ("+ str(DefaultKey) +")")
                N = DefaultKey

while True:
        try:
                I = str(input("rC >> "))


                if I.lower()=="encrypt":
                        msg = input("Input message (Type 'finish&exit' when done): ")+"\n"
                        while "finish&exit" not in msg:
                                msg = msg+input()+"\n"
                        msg = msg.split('finish&exit')[0]
                        encrypt = ""
                        for charX in msg:
                            encrypt = encrypt+str(int(F.index(charX)*N))+" "


                        try:
                            os.system('cls')
                        except:
                            os.system('clear')  
                        print("Encrypted Message: " + encrypt)
                elif I.lower()=="decrypt":      
                        msgToDecrypt = input("Input message: ")
                        decrypt=""
                        for char in msgToDecrypt.split(' '):
                                try:
                                        decrypt = decrypt+F[int(float(char)/N)]
                                except:
                                        decrypt = decrypt+str(random.choice(F))
                                                 
                        try:
                            os.system('cls')
                        except:
                            os.system('clear')
                        print("Decrypted message: "+decrypt)
                elif I.lower()=="cls" or I.lower()=="clear":
                        try:
                            os.system('cls')
                        except:
                            os.system('clear')
                elif "key" in I.lower():
                        try:
                                N = float(input("Enter New Key To Decrypt/Encrypt With: "))
                                print("New Key => "+ str(N))
                        except:
                                print("New Key is Invalid!")
                elif I.lower() == "help":
                        print("Available Commands: ")
                        print(" -> Help (Display this Menu)")
                        print(" -> Decrypt (Decrypt a Message using the current key)")
                        print(" -> Encrypt (Encrypt a Message using the current key)")
                        print(" -> key (Change the current key)")
                        print(" -> clear (Clear the Console)")
                else:
                        print("ERROR: Command not Recognized, List of Available Commands: ")
                        print(" -> Help (Display this Menu)")
                        print(" -> Decrypt (Decrypt a Message using the current key)")
                        print(" -> Encrypt (Encrypt a Message using the current key)")
                        print(" -> key (Change the current key)")
                        print(" -> clear (Clear the Console)")
                                  

        except:
                try:
                        print("Error while processing, please try again")
                        print("Possible values not in list: ") 
                        for l in msg:
                                if l not in F:
                                        print("'"+l+"',",end='')

                except:
                        print("ERROR: Please Review Your Input")                





