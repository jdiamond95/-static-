import argparse
import time
from lib.fileDetails import printDetailsCLI, getStrings
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
            elif command.startswith("strings"):
                command = command.split(" ")
                if len(command) > 1:
                    for string in getStrings(args.file, int(command[1])):
                        print(string)
                else:
                    for string in getStrings(args.file, 5): print(string)
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
                        - strings
                        - headers
                        - exit
                ''')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Static Malware Analysis")
    parser.add_argument('-f', "--file", help="File", type=str)
    parser.add_argument('-cli', "--cli", action='store_true', help="CLI Mode")
    args = parser.parse_args()
    main()
