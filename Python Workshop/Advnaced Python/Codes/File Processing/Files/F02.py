'''
practice file processing
'''

def main():
	with open('textfile_2','w') as f:
		f.write("Hello world\n")
		f.write("with statement takes care of file closing.\n")


main()

