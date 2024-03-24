from numpy import random
#参数是：可能的事件结果数量，结果概率列表，如骰子是n=6，概率是六个1/6
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)