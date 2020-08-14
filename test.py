def find_numbers(digit, start, end):
  final_answer = ""
  digit_str = str(digit)
  for i in range(start, end+1):
    i_str = str(i)
    if digit_str in i_str: final_answer += i_str + " "

  print(final_answer)

find_numbers(3, 5, 23)


liss = [[0]*6]
print(liss)
