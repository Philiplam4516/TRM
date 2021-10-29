'''
Write a program to repetively get strings from terminal until the 
string is "stop". Only new strings are kept and put into a list 
'''

def obtain_strings(list_str):
  while True:
    string=input("Enter string: ")
    if string == "stop":
    	break
    elif string not in list_str:
      list_str.append(string)
  return 

def main():

  list_str = []

  obtain_strings(list_str=list_str)
  print(list_str)

  return

main()