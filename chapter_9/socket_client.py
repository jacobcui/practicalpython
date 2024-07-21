# Client sending message to port 12345
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Connect to the server
s.connect((host, port))

# Send a message to the server
message = "Hello Server"
s.send(message.encode("ascii"))

# Receive data from the server
response = s.recv(1024)
print(response.decode("ascii"))

# Close the connection
s.close()
