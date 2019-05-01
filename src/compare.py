def compare(key, plaintext): #define Encryption function
        from keygen import keygen #importing Key Generation module
        from enc import enc #importing Encryption module
        from ecb_enc import ecb_enc #importing Encryption module

        for i in range (1,3):
                enc(key, plaintext, '../data/cbc_cipher'+str(i)+'.txt') #Calling enc function
                ecb_enc(key, plaintext, '../data/ecb_cipher'+str(i)+'.txt') #Calling enc function
