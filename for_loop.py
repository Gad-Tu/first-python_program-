number = [30, 10, 20]
total = 0
for item in number:
    total += item
print(f' total: {total}')
for item in range(1,6):
    print(f'{item} Mississippi')

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#this program is use to drawe a letter F by *.
name = [5, 2, 5, 2, 2]
for count in name:
    output = ''
    for gad in range(count):
        output += '*'
    print(output)