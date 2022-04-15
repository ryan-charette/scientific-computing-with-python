def arithmetic_arranger(problems):

  arranged_line1 = ""
  arranged_line2 = ""
  arranged_line3 = ""
  arranged_line4 = ""
  
  problem_list = eval(input("Enter arithmetic problem:"))
  for problems in problem_list:

    values = list()
    operands = problems.split()
  
    for value in operands:
      values.append(value)

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
      answer = str(int(values[0]) + int(values[2]))
    elif values[1] =="-":
      answer = str(int(values[0]) - int(values[2]))
    whitespace4 = " " * (length - len(answer))
    line4 = whitespace4 + answer

    arranged_line1 = arranged_line1 + line1 + "    "
    arranged_line2 = arranged_line2 + line2 + "    "
    arranged_line3 = arranged_line3 + line3 + "    "
    arranged_line4 = arranged_line4 + line4 + "    "

  arranged_problems = arranged_line1 + "\n" + arranged_line2 + "\n" + arranged_line3 + "\n" + arranged_line4
    
  return arranged_problems