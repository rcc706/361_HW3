#imports the required imports
import socket

#creating the socket for the server.
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#initilization of identifiers (ip and port #) and binds server to port 
cli.connect(('localhost', 9968))
print('The client has been connected')

#receives the 'connection was a sucess' message sent by the server 
print('The message from server.', cli.recv(256).decode())

print('Continue to provide the vectors to send to server...')

#user sends vector over to the server
while True:
    print('\nValid operators: + - *')
    print('+ for vector addition\n- for vector subtraction\n* for vector multiplication (cross-product)')
    msg = input('Please write the vector and the operation symbol (+ 1 2 3): ')
    cli.send(bytes(msg, encoding='utf8'))