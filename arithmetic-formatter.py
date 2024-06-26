def arithmetic_arranger(problems, show_answers=False):
    #Check if there are more than 5 input problems.
    if len(problems)>5:
        return 'Error: Too many problems.'
    output = ''
    operand_1, operand_2, operand_3, operand_4 = [], [], [], []
    for x, prob in enumerate(problems):
       #Split each problem into an array. Each operand is split by a ' '.
       arr = prob.split()
       length = max(len(arr[0]), len(arr[2]))
       #Dashes must span entire problem. +2 accounts for the operation and ' ' at the beginning of each second line.
       dashes = '-'*(length+2)

       #Check other error conditions.
       if arr[1] != '+' and arr[1] != '-':
           return "Error: Operator must be '+' or '-'."
       elif length > 4:
            return "Error: Numbers cannot be more than four digits."
       elif not (arr[0].isdigit() and arr[2].isdigit()):
           return 'Error: Numbers must only contain digits.'

       else:
        #Create buffers of ' ' characters for padding each line.
           buffer_1 = (abs(len(arr[0])-length)+2)*' '
           buf_1_length = len(arr[0])+2
           buffer_2 = abs(len(arr[2])-length)*' '
           buf_2_length = len(arr[2])+2
           if x < len(problems)-1:
               operand_1.append(f'{buffer_1}{arr[0]}    ')
               operand_2.append(f'{arr[1]} {buffer_2}{arr[2]}    ')
               operand_3.append(f'{dashes}    ')
               if show_answers and x==0:
                   if arr[1]=='+':
                      solution = int(arr[0])+int(arr[2])
                   elif arr[1]=='-':
                      solution = int(arr[0])-int(arr[2])
                   buffer_3 = abs(len(str(solution))-max(buf_1_length, buf_2_length))*' '
                   operand_4.append(f'\n{buffer_3}{solution}    ')
               elif show_answers and x!=0:
                   if arr[1]=='+':
                      solution = int(arr[0])+int(arr[2])
                   elif arr[1]=='-':
                      solution = int(arr[0])-int(arr[2])
                   buffer_3 = abs(len(str(solution))-max(buf_1_length, buf_2_length))*' '
                   operand_4.append(f'{buffer_3}{solution}    ')    
           else:
               operand_1.append(f'{buffer_1}{arr[0]}\n')
               operand_2.append(f'{arr[1]} {buffer_2}{arr[2]}\n')
               operand_3.append(f'{dashes}')
               if show_answers:
                   if arr[1]=='+':
                      solution = int(arr[0])+int(arr[2])
                   elif arr[1]=='-':
                      solution = int(arr[0])-int(arr[2])
                   buffer_3 = abs(len(str(solution))-max(buf_1_length, buf_2_length))*' '
                   operand_4.append(f'{buffer_3}{solution}')
    
    #Combine elements from each line into the output.
    for i in operand_1:
        output += i
    for j in operand_2:
        output += j
    for k in operand_3:
        output += k
    for l in operand_4:
        output += l
    return output

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
