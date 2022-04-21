def arithmetic_arranger(problems, answers = False):

  arranged_line1 = ""
  arranged_line2 = ""
  arranged_line3 = ""
  arranged_line4 = ""

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:

    values = list()
    operands = problem.split()
  
    for value in operands:
      if(len(value) <= 4):
        values.append(value)
      else:
        return "Error: Numbers cannot be more than four digits."

    length = 0
    whitespace1 = ""
    whitespace2 = " "
    line1 = ""
    line2 = ""
  
    if len(values[0]) > len(values[2]):
      length = len(values[0]) + 2
      whitespace1 = " " * (length - len(values[0]))
      whitespace2 = " " * (length - len(values[2]) - 1)
      line1 = whitespace1 + values[0]
      line2 = values[1] + whitespace2 + values[2]
    else:
      length = len(values[2]) + 2
      whitespace1 = " " * (length - len(values[0]))
      line1 = whitespace1 + values[0]
      line2 = values[1] + whitespace2 + values[2]
  
    line3 = length * "-"
    line4 = ""
    whitespace4 = ""
    answer = None
    if values[1] == "+":
      try:
        answer = str(int(values[0]) + int(values[2]))
      except:
        return "Error: Numbers must only contain digits."
    elif values[1] =="-":
      try:
        answer = str(int(values[0]) - int(values[2]))
      except:
        return "Error: Numbers must only contain digits."
    else:
      return "Error: Operator must be '+' or '-'."
    whitespace4 = " " * (length - len(answer))
    line4 = whitespace4 + answer

    arranged_line1 = arranged_line1 + line1 + "    "
    arranged_line2 = arranged_line2 + line2 + "    "
    arranged_line3 = arranged_line3 + line3 + "    "
    arranged_line4 = arranged_line4 + line4 + "    "

  arranged_problems = arranged_line1.rstrip() + "\n" + arranged_line2.rstrip() + "\n" + arranged_line3.rstrip()
  if answers == True:
    arranged_problems = arranged_problems + "\n" + arranged_line4.rstrip()
  return arranged_problems

#test  
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))