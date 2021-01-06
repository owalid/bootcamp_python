import sys

for arg in sys.argv[1:]:
  text = arg[::-1]
  final_text = ""
  for char in text:
    if char.islower():
      final_text += char.upper()
    else:
      final_text += char.lower()
  print(final_text)