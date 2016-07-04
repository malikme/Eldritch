import io
import socket
import struct
from PIL import Image
import numpy as np

importantInfo = open('importantInfo.txt','r')
myip = socket.gethostbyname(socket.gethostname())
ip = importantInfo.readline()[:-1]
port = int(importantInfo.readline()[:-1])
importantInfo.close()


server_socket = socket.socket()
server_socket.connect((myip, port))
#sampleImage = Image.(imageDirectory)

#This is from previous school project, sample code for image
matrix = np.zeros((320,320,3))

for i in range(320):
	for j in range(320):
		matrix[i,j]=[i,j,0]


#img = Image.fromarray(matrix, 'RGB')
#print len(str(matrix[0,0]))
#print str(matrix[0,0])

while True:
	for i in range(320):
		for j in range(320):
			toBeSent = str(matrix[i,j])
			print len(toBeSent)
			#while len(str(toBeSent)) < 19:
				#toBeSent = toBeSent + " "
			server_socket.send(toBeSent)

	break	
	


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
#    connection.close()
#    server_socket.close()