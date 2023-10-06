# import csv
# #немного помучался с кодировкой, так и должно быть)))? на стороннем сайте вбил текст из файла и он подсказал мне кодировку, на маке
# #он пытался воспринять его как utf-8
# with open('items.csv', 'r',  encoding='WINDOWS-1251') as csvfile:
#     diict = csv.DictReader(csvfile)
#     for line in diict:
#         print(line)
#
q = "5.5"
q = float(q)
q = int(q)
print(q)