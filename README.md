This python app allows you to gain access to your machines that may be behind a nat. I first built this program to gain access to my computer during the CCDC competition.

My computer was behind the school firewall and on a nated network. Without access to the firewall, I needed a way to gain access to my computer remotely. 

Out of lazyness and not wanting to leave my house to go to school, this program was developed.

This program provides shell access to a *nix based machine through IRC.


Security:

	This program will only take comments from a given name. 
	On that note, make sure to register the name you are going to use. 

Constraints:

	The output from all of the shell commands are limited by the number of inputs. 
	PUSH

Usage:

	python remote.py #Run this on the target machine


use the irc channel specified to connect.

Any text put into the room by the "Owner" will be executed as a shell command.

If you have this code running on more than one machine, direct a massage to a machine via

/msg machineUser commands