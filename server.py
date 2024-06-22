#making sure to import required modules 
import socket 
import threading
import numpy as np

#creating the socket for the server.
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket opened')

#initilization of identifiers (ip and port #) and binds server to port 
srv.bind(('localhost', 9968))
print('Bind to the local port')

# Setting server default vector
server_default_vector = [1.0, 1.0, 1.0]

#starts listening for incoming request from clients
srv.listen(5)
print('Started listening...')


##### function for the work for each incoming client ######
def NewClientSocketHandler(cli, ip):
    print('\nThe new client has socket id:', cli)
    while True:
        # prints the results 
        print('The message got for client socket:', cli)
        
        # Setting the client vector message to a variable
        client_vector = cli.recv(256).decode()
        
        # Splitting the client vector into an array
        arr = client_vector.split()
        new_arr = [float(arr[1]), float(arr[2]), float(arr[3])]
        
        # Checking for each operator and looping through the vector elements
        match arr[0]:
            case '+':
                for i in range(3):
                    new_vector = [new_arr[i] + server_default_vector[i] for i in range(3)]
            case '-': 
                for i in range(3):
                    new_vector = [new_arr[i] - server_default_vector[i] for i in range(3)]
            case '*':
                new_vector = np.cross(server_default_vector, new_arr)
            case default:
                print('ERROR! INVALID OPERATOR: %s' % arr[0])

        # Printing the information
        print('%s --- Client Vector: %s' % (cli, client_vector))
        print('%s --- New Vector: %s' % (cli, new_vector))
        
        

# loop that accepts the connection of each client and assigns the client connected to a new thread
while True:
    print('Waiting for the incoming connections')

    # accepts client
    cli, ip = srv.accept()
    cli.send(bytes('The connection was a success!' ,encoding='utf8'))

    #creates a new thread for each accepted/connected client
    threading._start_new_thread( NewClientSocketHandler, (cli, ip))