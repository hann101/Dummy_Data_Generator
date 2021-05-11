import random


f = open("s1.txt", 'r',encoding='utf-8')
lines = f.readlines()
hair_line = []
for line in lines:
    line = line.replace('\n','')
    hair_line.append(line)
f.close()
# a = random.randrange(1,7)

b=(random.choice(hair_line))
print(b)



# f = open("s1.txt", 'r',encoding='utf-8')
# lines = f.readlines()
# hair_line = []
# for line in lines:
#     line = line.replace('\n','')
#     hair_line.append(line)
# f.close()
# # for i in range(1,11):
# #     data = "%d번째 줄입니다.\n" % i
# #     f.write(data)
# # f.close()
# # print(hair_line)
# a = random.randrange(1,7)
# b = []
# for i in range(0,a):
#     b.append(random.choice(hair_line))
# print(b)