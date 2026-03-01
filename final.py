from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket and establish TCP connection
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()

    # Send HELO command
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command
    mailFrom = 'MAIL FROM:<alice@example.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command
    rcptTo = 'RCPT TO:<bob@example.com>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send message data followed by end message — NO recv between these
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv6 = clientSocket.recv(1024).decode()

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
