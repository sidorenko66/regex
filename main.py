from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)
print('=*'*60)
# TODO 1: выполните пункты 1-3 ДЗ
for row in contacts_list:

  result = re.findall(r'[\w]+', row[0])
  if not row[2] and not row[1] and len(result) == 3:
    row[0], row[1], row[2] = result[0], result[1], result[2]
  elif not row[1] and len(result) == 2:
    row[0], row[1] = result[0], result[1]

  result = re.findall(r'[\w]+', row[1])
  if not row[2] and len(result) == 2:
    row[1], row[2] = result[0], result[1]

  pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{1})[-\s]*(\d{1})[-\s]*(\d{1})[-\s]*(\d{1})[-\s]*(\d{1})[-\s]*(\d{1})" \
            r"[-\s]*(\d{1})( ?)([\s.\(]*)(доб.)?\s*(\d*)[ .\)]*"
  substitution = r"+7(\2)\3\4\5-\6\7-\8\9\10\12\13"
  result = re.findall(pattern, row[5])
  row[5] = re.sub(pattern, substitution, row[5])
  if result:
    result2 = re.sub(pattern, substitution, row[5])

cols_number = len(contacts_list[0])
contacts_list_dict = dict()
for row in contacts_list:
  if (row[0], row[1]) not in contacts_list_dict:
    contacts_list_dict[(row[0], row[1])] = row
  else:
    for i in range(cols_number):
      if not contacts_list_dict[(row[0], row[1])][i]:
        contacts_list_dict[(row[0], row[1])][i] = row[i]

contacts_list = list(contacts_list_dict.values())
pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',', lineterminator="\n")
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
