from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
print("establishing mailserver\n")
mailserver = ('smtp.mail.yahoo.com', 587 )

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
print("creating socket\n")
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
print("sending mail")
mailFrom = "MAIL FROM: <johnhoang5@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: "+recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
print("receiving mail")
rcptTo = "RCPT TO: <@epicturtlesfloat@aol.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: "+recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: "+recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send("QUIT\r\n".encode())
clientSocket.close()
# Fill in end
