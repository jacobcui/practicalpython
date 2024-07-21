# Socket server listening to port 12345
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Bind to the port
s.bind((host, port))

# Now wait for client connection
s.listen(5)

print("Server listening on {}:{}".format(host, port))

while True:
    # Establish connection with client
    client_socket, addr = s.accept()
    print("Got a connection from {}".format(addr))

    # Send a thank you message to the client
    message = "Thank you for connecting"
    client_socket.send(message.encode("ascii"))

    # Close the connection with the client
    client_socket.close()
