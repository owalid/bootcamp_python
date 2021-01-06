def text_analyzer(text):
  up_case = 0
  lower_case = 0
  punctuation = 0
  space = 0
  for char in text:
    if char == '.' or char == ',' or char == ';' or char == ':':
      punctuation += 1
    elif char == ' ':
      space += 1
    elif char.islower():
      lower_case += 1
    elif char.isupper():
      up_case += 1
  total = up_case + lower_case + punctuation + space
  print("The text contains %s characters:\n-- %s upper letters\n-- %s lower letters\n-- %s punctuation marks\n-- %s spaces" % (str(total), str(up_case), str(lower_case), str(punctuation), str(space)))
