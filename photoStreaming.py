import socket
import subprocess
import vlc


# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
socket.setdefaulttimeout(10)
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)


# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
Instance = vlc.Instance()
player = Instance.media_player_new()
try:
    # Run a viewer with an appropriate command line. Uncomment the mplayer
    # version if you would prefer to use mplayer instead of VLC
    #cmdline = 
    #cmdline = ["Preview", '--demux', 'h264', '-']
    #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
    
       
    player = subprocess.Popen('//Applications/VLC.app/Contents/MacOS/VLC', stdin=subprocess.PIPE)
    while True:
        # Repeatedly read 1k of data from the connection and write it to
        # the media player's stdin
        data = connection.read(1024)
        if not data:
            break
        #player.stdin.write(data)
        Media = Instance.media_player_new(data)
        #Media.get_mrl()
        #player.set_media(Media)
        #player.play()
finally:
    connection.close()
    server_socket.close()
    #player.terminate()