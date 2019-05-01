def keygen(newkey): #define Key Generation function
        from Crypto import Random
        #k = rndfile.read(32) #Generating a random key of 256 bits
        #sk = hex(int.from_bytes(k, byteorder='big', signed=False))
        sk = hex(int.from_bytes(Random.new().read(32), byteorder='big', signed=False))
        f = open(newkey,'w') #Opening the newkey.txt file in write mode
        f.write(sk) #Writing the New Key
        print('Key:'+'   '+sk) #Printing the New Key to command prompt
        #print('Key:'+'   '+str(k))
        f.close() #Closing the newkey.txt file
