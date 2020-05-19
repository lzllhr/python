# 将输入句子框起来
sentence = input("sentence is: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)//2
print()
print(left_margin*' '+'+'+'-'*box_width+'+')
print(left_margin*' '+'|'+box_width*' '+'|')
print(left_margin*' '+'|'+3*' '+sentence+3*' '+'|')
print(left_margin*' '+'|'+box_width*' '+'|')
print(left_margin*' '+'+'+'-'*box_width+'+')
print()