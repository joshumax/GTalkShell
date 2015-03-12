#!/usr/bin/python
# -*- coding: utf-8 -*-

# GTalkShell: Command your server over Google Talk/Hangouts
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Homepage: http://github.com/joshumax/GTalkShell
#

import sys
import subprocess
import os
import threading
import time
import signal
from PyGtalkRobot import GtalkRobot

class GTalkShell(GtalkRobot):

    def print_line(self, user):
	while True:
	    if self.process != None:
	        res = self.process.stdout.read()
		self.process.wait()
		if res != "":
	            self.replyMessage(user, res)
	return # Explicit return

    def command_100_default(self, user, message, args):
	'''.*?(?s)(?m)'''
	if self.p_t == None:
	    self.p_t = threading.Thread(target=self.print_line, args=(user,))
            self.p_t.daemon = True
            self.p_t.start()

	print("CMD: " + message)

	if self.process != None:
	    self.process.poll()
	    self.process_ret = self.process.returncode;
		
	if self.process_ret == None:
	    # Process is still running
	    if message.upper() == "^C":
		print("Sending SIGINT to process")
		return os.killpg(self.process.pid, signal.SIGINT)
	    elif message.upper() == "^Z":
		print("Sending SIGSTP to process")
		return os.killpg(self.process.pid, signal.SIGSTP)
	    elif message.upper() == "^\\":
		print("Sending SIGQUIT to process")
		return os.killpg(self.process.pid, signal.SIGQUIT)
	    else:
	    	self.process.stdin.write(message)
	else:
	    # Process is not running
	    l_msg = message.split(" ")
	    if l_msg[0] == "cd" and len(l_msg) >= 2:
		try:
		    return os.chdir(l_msg[1])
		except OSError as e:
		    return self.replyMessage(user,
			    "Unable to cd to " + l_msg[1])

	    try:
	        self.process = subprocess.Popen(
    	            message,
		    stdout=subprocess.PIPE,
		    stderr=subprocess.STDOUT,
    		    stdin=subprocess.PIPE,
		    shell=True,
		    preexec_fn=os.setsid)
	    except OSError as e:
	 	return self.replyMessage(user,
			"Unable to run " + message)

    def setupBot(self):        
        if len(sys.argv) <= 1:
            file = "login.txt"
        else:
            file = sys.argv[1]

        with open(file, "r") as t:
	    token = t.read()
	    self.userpass = token.split(':', 1)

	self.process = None
	self.process_ret = True
	self.p_t = None
    	self.setState('available', "GTalkShell Instance")
    	self.start(self.userpass[0], self.userpass[1])

    def shellInit(self):
	print("Starting shell...")
	self.setupBot()

if __name__ == "__main__":
    shell = GTalkShell()
    shell.shellInit()
