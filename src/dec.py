def dec(key, iv, ciphertext, result): #define Decryption function
        from Crypto import Random
        from Crypto.Cipher import AES
        from Crypto.Util import Padding

        f1 = open (key,'r') #Opening the key.txt file in read mode
        sk_hex = f1.read()
        f1.close() #Closing the key.txt file
        print(str(len(sk_hex)))
        sk = int(sk_hex,16).to_bytes(32, byteorder='big')
        #sk = (f1.read()).strip('\n') #Reading the Secret Key
        
        f2 = open (iv,'r') #Opening the iv.txt file in read mode
        iv_hex = f2.read()
        f2.close() #Closing the iv.txt file
        print(str(len(iv_hex)))
        iv = int(iv_hex,16).to_bytes(16, byteorder='big')
        #iv = (f2.read()).strip('\n') #Reading the Initialization Vector
        
        
        f3 = open (ciphertext,'r') #Opening the ciphertext.txt file in read mode
        cipher_hex = f3.read()[2:] #Reading the Cipher Message
        cipher = int(cipher_hex,16).to_bytes(int(len(cipher_hex)/2), byteorder='big')
        print(str(len(cipher)))

        
        f3.close() #Closing the ciphertext.txt file
        
        
        
        obj = AES.new(sk, AES.MODE_CBC, iv)
        padded_message = obj.decrypt(cipher)
        message = Padding.unpad(padded_message, 16, 'pkcs7')
        print(message.decode()) #Printing the Decrypted Message to command prompt
        
        f4 = open(result,'w') #Opening the result.txt file in write mode
        f4.write(message.decode()) #Writing the Decrypted Message
        
        f4.close() #Closing the result.txt file
