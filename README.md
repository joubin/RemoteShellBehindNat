This python script allows you to gain access to your machines that may be behind a nat or a firewall. I first built this program to gain access to my computer during the [CCDC](http://www.nationalccdc.org/) competition.

```

                                                                                                       +---------------+
                                                                     +-----------+                     |               |
                                                                     |           |           +---------+Target         |
                                                                     |           |           |         |               |
                                                                     |           |           |         +---------------+
                                                                     |           |           |         +---------------+
                                                                     |           |           |         |               |
+--------------+                                                     |           |           <---------+Target         |
|              |                                                     |           |           |         |               |
|You           +------------   Impossible Connection    ------------->           |           |         +---------------+
|              |                                                     |  Firewall |           |                          
+-------+------+                                                     |           |           |                          
        |                                                            |           |           |                          
        |                                                            |           |           |                          
        |                                                       +----------------------------+                          
        |                                                       |    |           |                                      
        |                                                       |    |           |                                      
        |                                                       |    +-----------+                                      
        |                                                       |                                                       
        |                                                       |                                                       
        |                                                       |                                                       
        |                                                       |                                                       
        |                                                       |                                                       
        |                                                       |                                                       
        |                                                       |                                                       
        |                                                +------v----------------------+                                
        |                                                |                             |                                
        |                                                |                             |                                
        |                                                |  IRC Server                 |                                
        +----------------------------------------------> |                             |                                
                                                         |                             |                                
                                                         |                             |                                
                                                         +-----------------------------+                                
```
My computers were behind the school firewall and on a nated network. Without access to the firewall, I needed a way to gain access to my computer remotely. 

Out of lazyness and not wanting to leave my apartment to go to school, this program was developed.

This program provides shell access to a *nix based machine through IRC.


Security:

	This program will only take commands from a given name. 
	On that note, make sure to register the name you are going to use. 

Constraints:

	The output from all of the shell commands are limited by the number of inputs. 
	PUSH

Usage:

	python Remote.py #Run this on the target machine


use the irc channel specified to connect.

Any text put into the room by the "Owner" will be executed as a shell command.

If you have this code running on more than one machine, direct a massage to a machine via

**Demo:**

Video: <iframe width="854" height="480" src="https://www.youtube.com/embed/s1T19g5X340" frameborder="0" allowfullscreen></iframe>

