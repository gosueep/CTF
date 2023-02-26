

file = open('timemachine.txt', 'r', encoding='utf8')
orig = open('The-Time-Machine.txt', 'r', encoding='utf8')

count = 0

for line in orig.readlines():
    line = line[:line.rfind('.')]
    if 'time' in line:
        count += 1

# for line in file.readlines():
#     line = line.strip()
#
#     line = line[:line.rfind('.')]
#
#     split = line.split(" ")
#
#     for i in split:
#         if 'time' in i:
#             count += 1
#
#     # while 'time' in line:
#     #     print("LINE START:")
#     #     print(line)
#     #     count += 1
#     #     line = line[line.find('time')+4:]
#     #
#     # print(count)
#     # print('\n\n\n')


print(count)
