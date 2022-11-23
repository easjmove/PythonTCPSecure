from socket import *
import ssl
import threading


def handle_client(connection_socket, address):
    print(address)

    sentence = connection_socket.recv(1024).decode()
    print(sentence)
    capitalized_sentence = sentence.upper()
    connection_socket.send(capitalized_sentence.encode())
    connection_socket.close()


serverPort = 7000
certificatesDirectory = 'C:/temp/'
privateKeyPath = certificatesDirectory + 'key.pem'
certificatePath = certificatesDirectory + 'certificate.pem'
privateKeyPassword = '1234'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=certificatePath, keyfile=privateKeyPath, password=privateKeyPassword)

serverSocket = socket(AF_INET, SOCK_STREAM, 0)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
secureSocket = context.wrap_socket(serverSocket, server_side=True)
print("Server is ready")
while True:
    connectionSocket, addr = secureSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()
