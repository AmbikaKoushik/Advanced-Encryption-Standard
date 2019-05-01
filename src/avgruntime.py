def avgruntime(key, iv, plaintext, ciphertext, result): #define Average Run Time for Encryption function
   from enc import enc #Importing enc module from enc.py
   from dec import dec
   import time #Importing time module
   enc_time = [0]*5 #Initializing an array of 5 integers
   dec_time = [0]*5 #Initializing an array of 5 integers
   for i in range(5): #Iterating the array
      enc_start = time.time() #Noting the Start time
      enc(key, plaintext, ciphertext) #Calling enc function
      enc_end = time.time() #Noting the end time

      dec_start = time.time() #Noting the Start time
      dec(key, iv, ciphertext, result) #Calling enc function
      dec_end = time.time() #Noting the end time
      
      enc_time[i] = enc_start - enc_end #Calculate the time elapsed for Encryption function
      dec_time[i] = dec_start - dec_end #Calculate the time elapsed for Encryption function
      print('Encryption time is '+ str(enc_time[i]) +' and Decryption time is '+ str(dec_time[i]))
      
   averageEncTime = sum(enc_time) / float(len(enc_time)) #Calculating the average time elapsed for Encryption function
   averageDecTime = sum(dec_time) / float(len(dec_time)) #Calculating the average time elapsed for Decryption function
   
   print('Average Run time for Encryption is ' +str(averageEncTime)+'s') #Printing the time elapsed for Encryption function on Command Prompt
   print('Average Run time for Decryption is ' +str(averageDecTime)+'s') #Printing the time elapsed for Decryption function on Command Prompt
