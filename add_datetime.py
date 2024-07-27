import datetime

current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

f = input()
with open(f, 'r') as file:
    lines = file.readlines()

if 'created' not in lines[3]:
    lines = lines[:3] + [f"    created: {current_time} IST\n"] + lines[3:]

with open(f, 'w') as file:
    file.writelines(lines)

print(f"Yup!")
