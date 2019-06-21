import os
import struct 
from boofuzz import *
import argparse
from swag import *
from boofuzz import *
from Fuzzing import FTP
from Fuzzing import HTTP1
from Fuzzing import VulnFuzz
from Fuzzing import SMTP
from swag import swags
import sys
import struct


def main():
    if len(sys.argv) < 2:
        swags.banner()
        print("enter -H for Help")
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--module',  help="Select a Module")
    parser.add_argument("--host", help="Select a host")
    parser.add_argument("--port", help="Select a port")
    parser.add_argument("--username", help='Use a username')
    parser.add_argument("--password", help='Use a password')
    args = parser.parse_args()
    if args.module == "help":
        swags.banner()
        print("Modules avaiable:\n")
        print("HTTP = HTTP Fuzzing\n")
        print("FTP = FTP Fuzzing\n")
        print("Vuln = VulnServer Fuzzing\n")
    if args.module == "HTTP":
        HTTP1.HTTP_Fuzzing(args.host, args.port)
    elif args.module == "FTP":
        args = parser.parse_args()
        FTP.FTP_Fuzzing(args.host, args.port, str(args.username), str(args.password))
    elif args.module == "Vuln":
        args = parser.parse_args()
        VulnFuzz.VulnServer(args.host, args.port)
    elif args.module == "SMTP":
        args = parser.parse_args()
        SMTP.SMTP_Fuzz(args.host, args.port)

if __name__ == "__main__":
     main()