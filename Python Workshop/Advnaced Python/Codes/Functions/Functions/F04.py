'''
Specify default values for input arguments
'''
def count_letter(string, letter=' '):
  count = 0
  for i in string:
      if i == letter:
        count = count + 1
  return count

def main():

  text = "I am learning python"
  num = count_letter(string=text)
  print("while space appears {} times \
    in {}".format(num, text))
  return

main()