from sys import argv
if len(argv) > 1:
	print(hex(int(argv[1])).replace("0x",'').upper())
else:
	from sys import platform
	if platform == "win32":
		print("Usage:\n\t{} dec_num".format(argv[0].split('\\')[-1]))
	else:
		print("Usage:\n\t{} dec_num".format(argv[0].split('/')[-1]))