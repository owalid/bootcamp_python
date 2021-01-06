import sys
def is_int(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False

usage = "Usage: python operations.py <number1> <number2>\nExample:\n   python operations.py 10 3"
err_args = "InputError: too many arguments"
err_float = "InputError: only numbers"

arg = sys.argv[1:]
len_arg = len(arg)

if len_arg > 3:
  print(err_args)
elif len_arg < 2:
  print(usage)
else:
  if is_int(arg[0]) and is_int(arg[1]):
    nb1 = int(arg[0])
    nb2 = int(arg[1])
    sum_nbs = str(nb1 + nb2)
    diff = str(nb1 - nb2)
    if nb2 == 0:
      quo = "ERROR (div by zero)"
      mod = "ERROR (modulo by zero)"
    else:
      quo = str(nb1 / nb2)
      mod = str(nb1 % nb2)
    print("Sum: %s\nDifference: %s\nQuotient: %s\nRemainder:  %s" % (sum_nbs, diff, quo, mod))
  else:
    print(err_float)