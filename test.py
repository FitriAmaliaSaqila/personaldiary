# belajar f string agar mengurangi sintax yang panjang menggunakan tanda plus

# first_name = 'joseph'
# last_name = 'choi'
# full_name = f'{first_name} {last_name}'
# print(full_name)

#  belajar python datetime

from datetime import datetime

today = datetime.now()

date_time = today.strftime('%Y-%m-%d-%H:%M:%S')

print(date_time)