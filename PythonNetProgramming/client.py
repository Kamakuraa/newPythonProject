import socket
from time import time

server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input_s = 'Hello, server!'.encode('utf8')

sent_time = time()  # time immediately before sending
client_socket.sendto(input_s, ('127.0.0.1', server_port))
input_s_modified, address = client_socket.recvfrom(65535)
recv_time = time()  # time after received response

client_socket.close()

print('[CLIENT] Response from server {}, is: "{}"'.format(address, input_s_modified.decode('utf8')))
print("elapsed time =", recv_time - sent_time, 'seconds')
