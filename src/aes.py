from enc import enc #importing Encryption module
from dec import dec #importing Decryption module
from keygen import keygen #importing Key Generation module
from ecb_enc import ecb_enc #importing Encryption module
from compare import compare #importing compare function to compare ecb and cbc ciphertexts
from avgruntime import avgruntime #importing Average Run Time for encryption module


if __name__ == '__main__': #calling main function
        import sys #importing sys module
        import os #importing os module
        #First argument i.e sys.argv[0] is always aes.py
        #Second argument i.e sys.argv[1] is the called function
        #Comparing the second command line argument with respective functions to call
        if sys.argv[1] == 'enc': #Comparing with enc
                enc(sys.argv[2], sys.argv[3], sys.argv[4]) #Calling enc function
        elif sys.argv[1] == 'ecb_enc': #Comparing with enc
                ecb_enc(sys.argv[2], sys.argv[3], sys.argv[4]) #Calling enc function
        elif sys.argv[1] == 'dec': #Comparing with dec
                dec(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]) #Calling dec function
        elif sys.argv[1] == 'keygen': #Comparing with keygen
                keygen(sys.argv[2]) #Calling keygen function
        elif sys.argv[1] == 'compare': #Comparing with keygen
                compare(sys.argv[2],sys.argv[3]) #Calling keygen function
        elif sys.argv[1] == 'avgruntime': #Comparing with avgruntime
                avgruntime(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]) #Calling avgruntime function
