f1 = open('text1.txt', 'r')
txt_1 = f1.read()
list_1 = txt_1.split(',')
#print(list_1)
f1.close()

#print('*\n' * 12)

f2 = open('text2.txt', 'r')
txt_2 = f2.read()
list_2 = txt_2.split(',')
#print(list_2)
f2.close()

new_list = list_1 + list_2
#print(new_list)

new_set = set(new_list)
#print(new_set)

final_list = list(new_set)
#print(final_list)

with open('text3.txt', 'w') as f3:
    for item in final_list:
        f3.write(item)
        f3.write(', ')