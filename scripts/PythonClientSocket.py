import socket

# HOST='104.131.54.221'
# PORT=443

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# 	s.connect((HOST,PORT))
# 	s.sendall(b'key') # sending in binary
# 	data=s.recv(1024) # Whatever server is sending

# print(data)

Host = '127.0.0.1'
Port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host,Port))