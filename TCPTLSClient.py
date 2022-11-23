from socket import *
import ssl

server_address = 'localhost'
serverPort = 7000

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

socket = create_connection((server_address, serverPort))
secureSocket = context.wrap_socket(socket, server_hostname="server")

sentence = input('Input sentence: ')
secureSocket.send(sentence.encode())
modifiedSentence = secureSocket.recv(1024).decode()
print('From server: ', modifiedSentence)
secureSocket.close()
