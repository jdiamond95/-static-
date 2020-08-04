import argparse
import time
from lib.fileDetails import printDetailsCLI
from lib.entropy import printEntropyCLI
from lib.virusTotal import printVTCLI
from lib.headers import magicBytes

banner = """
  /\//    __        __  _     /\//
 //\/____/ /_____ _/ /_(_)___//\/
   / ___/ __/ __ `/ __/ / ___/
  (__  ) /_/ /_/ / /_/ / /__
 /____/\__/\__,_/\__/_/\___/
 """


def main():
    if args.cli:
        print(banner)
        while (True):
            command = input("\n>>")
            if command == "details":
                printDetailsCLI(args.file)
            elif command == "entropy":
                printEntropyCLI(args.file)
            elif command == "virusTotal":
                printVTCLI(args.file)
            elif command == "headers":
                magicBytes(args.file)    
            elif command == "exit":
                break
            else:
                print('''
                    ===========CLI Mode============
                    Commands:
                        - details
                        - entropy
                        - virusTotal
                        - exit
                ''')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Static Malware Analysis")
    parser.add_argument('-f', "--file", help="File", type=str)
    parser.add_argument('-cli', "--cli", action='store_true', help="CLI Mode")
    args = parser.parse_args()
    main()
