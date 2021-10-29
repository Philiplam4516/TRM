'''
Write a program to repetively get strings from terminal until the 
string is "stop". Only new strings are kept and put into a list 
'''

def obtain_integers():
  # obtain inputs from ternminal
  list_integer = []
  while True:
    value=input("Enter positive integer: ")
    value=int(value)
    if value == 0:
    	break
    elif value not in list_integer:
      list_integer.append(value)
 
  # compute sum and product of elements in the list 
  summation = 0
  product = 1
  for value in list_integer:
    summation += value
    product *= value

  return list_integer, summation, product

def main():


  list_integer, summation, product = obtain_integers()

  print(list_integer)
  print("sum of the list is {}".format(summation))
  print("product of the list is {}".format(product))

  return

main()