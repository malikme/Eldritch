import io
import socket
import struct

from PIL import Image

importantInfo = open('importantInfo.txt','r') #opening file for read
ip = importantInfo.readline()[:-1] #[:-1] removes the last part of the line, which is the endline because messes up socket.bind
port = int(importantInfo.readline())
importantInfo.close()





# Start a socket listening for connections on IP address of pi and random port (8000)
# Bind tells the socket where to look and listen makes it start listening for an action from that ip
# The action should be connect.
server_socket = socket.socket()
server_socket.bind((ip, port))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it

connection = server_socket.accept()[0].makefile('rb')

print connection

print "SOCKET CONNECTION ESTABLISHED"


#try:
#   while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
#        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
#        if not image_len:
#            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
#        image_stream = io.BytesIO()
#        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
#        image_stream.seek(0)
#        image = Image.open(image_stream)
#        print('Image is %dx%d' % image.size)
#        image.verify()
#        print('Image is verified')
#finally:

connection.close()
server_socket.close()