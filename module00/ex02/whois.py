import sys

err = "ERROR"
odd = "I'm Odd."
even = "I'm Even."
zero = "I'm Zero."

arg = sys.argv[1:]
len_arg = len(arg)
if len_arg > 1 or len_arg == 0:
  print(err)
else:
  number = arg[0]
  if number.isnumeric():
    if number == "0":
      print(zero)
    elif int(number) % 2 == 0:
      print(odd)
    else:
      print(even)
  else:
    print(err)