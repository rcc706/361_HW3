# 361 - HW3

2022-2023 Spring Semester

This is my multi-threaded client-server program that asks a user for a vector along with an operator. Then, it adds/subtracts/cross-product the servers' vector (1, 1, 1) to it, and prints the new vector (along with the client information) on the server-side terminal instance. 

## Modules
The following modules that were installed for this program are listed below: 
- socket: Socket programming. 
- threading: Multiple threads. 
- numpy: Cross product between vectors. 

## Compilation
1. Open VScode and split the terminals, or use multiple instances of command line. 
2. Change your directory of both terminal instances to that of which this project folder is saved to
3. In one terminal instance, type the following into the command line: 
    ```python server.py```
    - The following will display: 
        ```
            Server socket opened
            Bind to the local port
            Started listening...
            Waiting for the incoming connections
        ```
4. In the clients' terminal instance, type the following into the command line:
    ```python client.py```
5. In the clients' terminal isntance, the following prompt will display:
    ```
        The client has been connected
        The message from server. The connection was a success!     
        Continue to provide the vectors to send to server...       
        
        Valid operators: + - *
        + for vector addition
        - for vector subtraction
        * for vector multiplication (cross-product)
        Please write the vector and the operation symbol (+ 1 2 3):
    ```

## Results

The following will be the result on the clients' terminal after a vector input is entered: 
```
    The client has been connected
    The message from server. The connection was a success!     
    Continue to provide the vectors to send to server...       

    Valid operators: + - *
    + for vector addition
    - for vector subtraction
    * for vector multiplication (cross-product)
    Please write the vector and the operation symbol (+ 1 2 3): * 2 3 4

    Valid operators: + - *
    + for vector addition
    - for vector subtraction
    * for vector multiplication (cross-product)
    Please write the vector and the operation symbol (+ 1 2 3):
```

The following will be the result on the servers' terminal after a vector input has been entered a client: 
```

    The new client has socket id: <socket.socket fd=436, family=2, type=1, proto=0, laddr=('127.0.0.1', 9968), raddr=('127.0.0.1', 53294)>The message got for client socket: <socket.socket fd=436, family=2, type=1, proto=0, laddr=('127.0.0.1', 9968), raddr=('127.0.0.1', 53294)>
    <socket.socket fd=436, family=2, type=1, proto=0, laddr=('127.0.0.1', 9968), raddr=('127.0.0.1', 53294)> --- Client Vector: + 2 2 2   
    <socket.socket fd=436, family=2, type=1, proto=0, laddr=('127.0.0.1', 9968), raddr=('127.0.0.1', 53294)> --- New Vector: [3, 3, 3]    
    The message got for client socket: <socket.socket fd=436, family=2, type=1, proto=0, laddr=('127.0.0.1', 9968), raddr=('127.0.0.1', 53294)>
```

As shown above, the clients' vector (sent message to server) was '+ 2 2 2'. 
```
    --- Client Vector: + 2 2 2
```

After adding the default server vector (1, 1, 1) to the clients' vector (2, 2, 2): 
```
    --- New Vector: [3, 3, 3]
```