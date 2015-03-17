# GTalkShell

## About:

GTalkShell allows you to send commands to a POSIX-compliant Operating System over Google Talk/Hangouts... You know, for all those times you wish that you could remotely control your home server or something in the most horrific way possible.

This application was originally designed to allow me to "SSH" into my Raspberry Pi on an old dumb-phone that only had a really poorly-built messaging client built into it. Luckily said messaging client somehow allowed for sending messages over Google Talk. After finishing the project, however, I decided I'd put it on GitHub for its novelty. Feel free to set this up on your server for whatever you'd want to use it for.

## Installation:

* Create a Google account for yourself if you haven't already
* Install Python 2.7+
* Install xmpppy
* Install pydns
* Clone this repository
* Create a new Google account for your server
* Set the appropriate auth details in 'login.txt'
* Login as the server in your web browser
* MAKE SURE MESSAGES CAN ONLY COME FROM PEOPLE IN YOUR CIRCLES!
* Add yourself to your server's friend circle
* Logout
* Login as youself again
* Add your server to your friend circle
* Run the 'shell.py' on your server
* Start messaging away on Google Hangouts

## Limitations:

Programs that rely on STDIN instead or parameters won't show their output until they complete. This is due to the fact that Google Talk is not a character device and STDIN was architectually designed for character devices. You can still input to STDIN, but you won't see any output until execution completes. This is also a problem for programs that may not use STDIN but take a long time to complete, i.e. 'make' or something like it. If you run one of these programs by accident symply type "^C" (as-is) and GTalkShell will send SIGINT to the running process to kill it. Also, environment variables aren't preserved amongst commands.

## Images:

![I have no idea](https://sbgt.us/u/e4ceddee6fc1f5c91ea3a.png)
