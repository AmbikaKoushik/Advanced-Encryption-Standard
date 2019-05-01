def enc(key, plaintext, ciphertext): #define Encryption function
        from Crypto import Random
        from Crypto.Cipher import AES
        from Crypto.Util import Padding
        
        f1 = open (key,'r') #Opening the key.txt file in read mode
        sk_hex = f1.read()
        f1.close() #Closing the key.txt file
        sk = int(sk_hex,16).to_bytes(32, byteorder='big')
        #sk = (f1.read()).strip('\n') #Reading the Secret Key
        
        f2 = open (plaintext,'r') #Opening the plaintext.txt file in read mode
        message = (f2.readline()).strip('\n') #Reading the PlainText/Message
        f2.close() #Closing the plaintext.txt file
        
        iv = Random.new().read(16)
        iv_hex = hex(int.from_bytes(iv, byteorder='big', signed=False))

        f3 = open('../data/iv.txt','w') #Opening the IV.txt file in write mode
        f3.write(iv_hex) #Writing the iv
        f3.close()
        print(iv_hex) #Printing the iv to command prompt
        
        obj = AES.new(sk, AES.MODE_CBC, iv)
        padded_message = Padding.pad(str.encode(message), 16, 'pkcs7')

        #print(len((padded_message)))
        cipher = obj.encrypt(padded_message)
        cipher_hex = hex(int.from_bytes(cipher, byteorder='big', signed=False))

        f4 = open(ciphertext,'w') #Opening the ciphertext.txt file in write mode
        f4.write(cipher_hex) #Writing the CipherText
        f4.close() #Closing the ciphertext.txt file
        print(cipher)
        print(cipher_hex) #Printing the CipherText to command prompt
