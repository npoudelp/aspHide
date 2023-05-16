# aspHide

A CLI based steganography tool, that has functionality of inserting text messages in jpg and jpeg image.
This program uses the two bit of LSB of the R channel of each pixel of selected image to hide the binary encoded
message, provided by users. It takes password from user while hiding message which has to be verified by receiver inorder to see
the hidden message. The password is than hashed and message is encrypted with the password. Then hashed password and 
encrypted message are combined to form a long string. The string is then hidden in image.<br>
The process is reverserd to display the unencrypted message upon the insertion of correct password by receiver.

This program is designed to run in terminal of linux machine. Other os may not support the file handling
process that is used in the program.

If you have any suggestion, feel free to leave it. <a href="https://nirojpoudel.com.np/pages/contact.php">here</a>

<h3><u>Using aspHide</u></h3>
- <i>python main.py</i>  :main.py is the index file for the program.<br>
- Selecting file process automatically detects the selected file type and accepts only jpg or jpeg file and changes directory if dir is selected.<br>
- [{^] is used as escape sequence for password which denotes the end of password. So, don't type [{^] in password.<br>
- [END] is used as escape sequence that detects the end of message. So, don't type [END] in message.<br>
- Once the message is hidden into image, you will be redirected to main menu and image saved directory will be shown. (~/)<br>
- To see the hidden message user needs to provide the decryption key, and only gets a single try do so.<br> 
- Once the message is extracted from the image, the message is displayed in the terminal and asks for input.<br>
- w! -> to write the text to a file in ~/ dir<br>
- q! -> exit without saving the file

<h3><u>Library used from Python</u></h3>
- PIL<br>
- OS<br>
- time<br>
