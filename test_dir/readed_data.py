from random import shuffle, choice
from time import sleep

# MAILS
with open('../data/mails.txt', 'r') as file:
    mails = file.read().split('\n')

# Взболтать
shuffle(mails)

# # Цикл проверки на пустые значения
# for i in mails:
#     if i == '':
#         mails.remove(i)

# # Перезаписываем без забранного значения
# with open('../data/mails.txt', 'w') as file:
#     # Цикл записи данных
#     for i in mails:
#         file.write(i + '\n')
#



# PASSWORDS
with open('../data/passwords.txt') as file:
    passwords = file.read().split('\n')

# # ZIP CODES USA
# with open('../data/zip_codes.txt') as file:
#     zip_codes = file.read().split('\n')

print(choice(mails))
print(choice(passwords))