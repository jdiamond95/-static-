import argparse
import time
# from lib.fileDetails import getFileSize


banner = """
  /\//    __        __  _     /\//
 //\/____/ /_____ _/ /_(_)___//\/
   / ___/ __/ __ `/ __/ / ___/
  (__  ) /_/ /_/ / /_/ / /__
 /____/\__/\__,_/\__/_/\___/
 """



def main():
	print(getFileHash(args.file, "MD5"))
	print(getFileHash(args.file, "SHA256"))
	print(getFileHash(args.file, "SHA1"))


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Static Malware Analysis")
	parser.add_argument('-f', "--file", help="File", type=str)
	args = parser.parse_args()
	main()
