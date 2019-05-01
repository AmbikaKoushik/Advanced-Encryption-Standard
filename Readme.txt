I am using the python language for this project. Since python is an interpreted language no compiler is needed to run the code.

Steps followed for the execution:

1. Install Python 3 using the below command
sudo apt-get install python3.6

2. Verifying the python version using the below command
python3 --version

3. By default when you call the 'python' keyword in Linux terminal python2 will be invoked. To open python3 with 'python' keyword use the below command:
cd ~
sudo gedit .bashrc

4. Add the below line at the end of the file
alias python=python3

5. save and close the file

6. Go to terminal and excute the below command:
source ~/.bashrc

7. Go to /aes_m12507845/build/pycrypto-master folder and execute the below commands to add PyCrypto library to your local

python setup.py build" to build the package
and "python setup.py install" to install it.


8. Go to Source folder: /otp_m12507845/src



9. Execute the below commands for respective functions :



a) For running the Encryption function, execute the below command:
python otp.py enc ../data/key.txt ../data/plaintext.txt ../data/ciphertext.txt



b) For running the Decryption function, execute the below command:
python otp.py dec ../data/key.txt ../data/ciphertext.txt ../data/result.txt



c)For running the Key generation function, execute the below command:
python otp.py keygen 100 ../data/newkey.txt



d) For running the Frequency Distribution function for the key lenth equal to 3, execute the below command:
python otp.py freqdist 3 ../data/record.txt



e) For finding the average run time of the encryption function for the key lenght of 128bits, execute the below command:
python otp.py avgruntime 128 ../data/key128.txt ../data/plaintext128.txt ../data/ciphertext128.txt
