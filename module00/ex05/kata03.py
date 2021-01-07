phrase = "The right format"

len_phrase = len(phrase)
final_string = ""
diff_len = 42 - len_phrase

for _ in range(diff_len):
  final_string += "-"

print(final_string + phrase, end='', flush=True)