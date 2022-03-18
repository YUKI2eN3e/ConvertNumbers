from sys import argv
if len(argv) > 1:
	print(int(argv[1],2))
else:
	from sys import platform
	if platform == "win32":
		print("Usage:\n\t{} bin_num".format(argv[0].split('\\')[-1]))
	else:
		print("Usage:\n\t{} bin_num".format(argv[0].split('/')[-1]))