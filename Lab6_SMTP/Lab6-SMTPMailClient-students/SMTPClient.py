# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

from socket import *
import argparse as ap
import getpass as gp

#Get sender_email and recipient_email as arguments to the program
parser = ap.ArgumentParser(description='A test SMTP client without authentication')
parser.add_argument('-f', '--from', dest='fromMail', required=True, metavar='<sender_email>')
parser.add_argument('-t', '--to', dest='toMail', required=True, metavar='<recipient_email>')
#If using the authentication of the SMTP server, also get a valid username (optional exercise)
#parser.add_argument('-u', '--username', dest='username', required=True, metavar='<username>')

args = parser.parse_args()
fromMail = args.fromMail #Sender's email address
toMail = args.toMail #Recipient's email address
#username = args.username #SMTP username in case you are implementing the optional exercise

#If using the authentication of the SMTP server, ask for a valid password (optional exercise)
#password = gp.getpass(prompt='Password: ')

# Message to send
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no but it allows only authenticated communications. (optional exercise)
#mailserver = 'smtp.stud.ntnu.no'
# You can run a local simple SMTP server such as "Fake SMTP Server" and communicate with it without authentication.
mailserver = 'localhost'

# Create socket called clientSocket and establish a TCP connection
# (use the appropriate port) with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
port = 25
clientSocket.connect((mailserver,port))
#Fill in end

recv = clientSocket.recv(1024)
print(recv.decode())
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
# Can use EHLO instead since HELO is obsolete, but the latter can still be used
heloCommand = 'EHLO Hey\r\n'
clientSocket.send(heloCommand.encode()) #Python 3
#clientSocket.send(heloCommand) #Python 2.7
recv1 = clientSocket.recv(1024)
print(recv1.decode())
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM:' + str(fromMail) + '\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo ='RCPT TO:' + str(toMail) + '\r\n'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
print(recv3.decode())
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
print(recv4.decode())
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT\r\n'.encode())
recv6 = clientSocket.recv(1024)
print(recv6.decode())
clientSocket.close()
# Fill in end

#Note that there are more communications if you implement the optional exercise.
