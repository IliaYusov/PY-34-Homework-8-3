import os

dirs = [file for file in os.listdir(os.getcwd()) if file.endswith('.txt') and file != 'joined.txt']

joined = []

for file in dirs:
    with open(file, 'r', encoding='utf-8') as f_in:
        text = f_in.readlines()
        joined.append((len(text), file, ''.join(text)))

with open('joined.txt', 'w+', encoding='utf-8') as f_out:
    for file in sorted(joined):
        f_out.write(file[1] + '\n' + str(file[0]) + '\n' + ''.join(file[2]))
