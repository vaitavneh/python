'''
text = ' my first python program'
saveFile = open('program.txt','w')
saveFile.write('text')
saveFile.close()
'''
'''
appendMe = ' this is second program'
appendFile = open('program.txt','a')
appendFile.write(appendMe)
appendFile.close()
'''

'''
readMe = open('program.txt','r').read()
print(readMe)
'''

'''
x = raw_input(' whats your name')
print(x)

'''


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
server ='amazon.net'
port = 80
server_ip = socketgethostbyname(server)
print(server_ip)



