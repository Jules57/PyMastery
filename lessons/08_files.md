### Работа с файлами

Программа на Python — это не только функционал, но и оптимальная система работы с файлами. Например, если вы пишете
чат-бот, вам нужно загрузить в него готовые ответы в файле txt. Если вы сделали программу для обработки фото — здесь ваш
код на Python должен быть готов обрабатывать файлы, которые загрузит в сервис пользователь.

# Что такое файл

На любом компьютере и в любой операционной системе есть файлы — область данных со своим именем, хранящаяся на носителе.
Их принято считать базовыми объектами, из которых складываются директории. В Python с помощью файлов можно сохранять
результат работы программы или получать из них данные для обработки в коде.

С любыми файлами можно производить действия, которые делятся на три группы:

1. открытие;
2. операции чтения из файла и записи в файл;
3. закрытие.

Разберемся со всеми действиями по порядку.

Работа с файлами - важная часть программирования в Python. В этом уроке мы рассмотрим основные операции чтения и записи
файлов, а также различные способы работы с текстовыми и бинарными файлами в Python.

# Типы файлов

В Python все файлы делятся на:

- Текстовые 't'
- Бинарные (двоичные) 'b'

Если никакой определенный тип файла не указан, по умолчанию Python считает, что пользователь работает с текстовыми
файлами. Поэтому для работы с изображениями, мультимедийными файлами и pdf, например, следует указывать, что тип файла
относится к 'b'.

Итак, начнем. Прежде, чем работать с файлом, его надо открыть. С этим замечательно справится встроенная функция open:

```python
f = open('text.txt', 'r')
```

У функции `open()` много параметров, нам пока важны 3 аргумента: первый - это имя (путь) файла. Путь к файлу может быть
относительным или абсолютным. Второй аргумент, это режим, в котором мы будем открывать файл.

| Режим | Обозначение                                                                                |
|-------|--------------------------------------------------------------------------------------------|
| 'r'   | открытие на чтение (является значением по умолчанию).                                      |
| 'w'   | открытие на запись, содержимое файла удаляется, если файла не существует, создается новый. |
| 'x'   | открытие на запись, если файла не существует, иначе исключение.                            |
| 'a'   | открытие на дозапись, информация добавляется в конец файла.                                |
| 'b'   | открытие в двоичном режиме.                                                                |
| 't'   | открытие в текстовом режиме (является значением по умолчанию).                             |
| '+'   | открытие на чтение и запись                                                                |

Режимы могут быть объединены, то есть, к примеру, 'rb' - чтение в двоичном режиме. По умолчанию режим равен 'rt'.

И последний аргумент, `encoding`, нужен только в текстовом режиме чтения файла. Этот аргумент задает кодировку.

# Методы работы с файлами

| Метод                 | Что делает                                           |
|-----------------------|------------------------------------------------------|
| file.read(size)       | 	Прочитать определенное количество символов из файла |
| file.readline()       | 	Прочитать строку из файла                           |
| file.readlines()      | 	Прочитать все строки из файла                       |
| file.write(string)    | 	Записать строку в файл                              |
| file.writelines(list) | 	Записать список строк в файл                        |
| file.seek(int)        | 	Переместить указатель                               |
| file.tell()           | 	Узнать текущее положение указателя                  |

# Чтение из файла

Открыли мы файл, а теперь мы хотим прочитать из него информацию. Для этого есть несколько способов, но большого интереса
заслуживают лишь два из них.

Первый - метод `read()`, читающий весь файл целиком, если был вызван без аргументов, и `n` символов, если был вызван с
аргументом (целым числом n).

```python
f = open('text.txt')
f.read(1)
'H'
f.read()
'ello world!\nThe end.\n\n'
```

Ещё один способ сделать это - прочитать файл построчно, воспользовавшись циклом for:

```python
f = open('text.txt')
for line in f:
    line

'Hello world!\n'
'\n'
'The end.\n'
'\n'
```

Можно прочитать определенное количество символов из файла с помощью метода `read()` с аргументом:

```python
file = open("example.txt", "r")
partial_content = file.read(50)  # Прочитать первые 50 символов файла
file.close()
```

Также файлы можно открывать с помощью менеджера контекста `with`. В этом случае файл автоматически закроется, когда
работа с ним завершится:

```python
with open("example.txt", "w+", encoding="utf-8") as infile:
# actions with file
```

Все строки файла можно прочитать с помощью метода `readlines()`, возвращающего содержимое в виде списка вместе со
специальными символами:

```python
with open('file.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
print(data)
# ['Carrot\n', 'Cream\n', 'Sugar\n', 'Apples']
```

Такое чтение можно реализовать и без метода `readlines()`, воспользовавшись конструктором списков `list()`:

```python
with open('file.txt', 'r', encoding='utf-8') as f:
    data = list(f)
print(data)
# ['Carrot\n', 'Cream\n', 'Sugar\n', 'Apples']
```

При чтении всего файла в Python стоит помнить, что он может быть слишком большим. Если разместить его полностью в
оперативной памяти компьютера не получается, следует считывать его частями.

# Запись в файл

Теперь рассмотрим запись в файл. Попробуем записать в файл вот такой вот список:

```python
# Откроем файл на запись:
f = open('text.txt', 'w')

my_list = [str(i) + str(i - 1) for i in range(20)]
my_list
# ['0-1', '10', '21', '32', '43', '54', '65', '76', '87', '98', '109', '1110', '1211', '1312', '1413', '1514', '1615', '1716', '1817', '1918']

# Запись в файл осуществляется с помощью метода write:
for index in my_list:
    f.write(index + '\n')

# 4
# 3
# 3
# 3
# 3
```

Для тех, кто не понял, что это за цифры, поясню: метод `write()` возвращает число записанных символов.

Если файл не существует, он будет создан. Если файл существует, его содержимое будет заменено.

После окончания работы с файлом его обязательно нужно закрыть с помощью метода `close()`. Закрытие файла важно, чтобы
освободить ресурсы и обеспечить целостность данных.:

```python
f.close()
``` 

Теперь попробуем воссоздать этот список из получившегося файла. Откроем файл на чтение (надеюсь, вы поняли, как
это сделать?), и прочитаем строки.

```python
f = open('text.txt', 'r')
my_list = [line.strip() for line in f]
my_list
['0-1', '10', '21', '32', '43', '54', '65', '76', '87', '98', '109', '1110', '1211', '1312', '1413', '1514', '1615',
 '1716', '1817', '1918']
f.close()

```

Мы получили тот же список, что и был. В более сложных случаях (словарях, вложенных кортежей и т. д.) алгоритм
записи придумать сложнее. Но это и не нужно. В python уже давно придумали средства, такие как pickle или json,
позволяющие сохранять в файле сложные структуры.

## Запись в Файл

Для записи текста в файл используйте режим доступа "w" (запись) с функцией `write()`:

```python
file = open("example.txt", "w")
file.write("Привет, мир!")
file.close()
```

Если файл не существует, он будет создан. Если файл существует, его содержимое будет заменено.

## Работа с бинарными файлами

Все вышеупомянутые операции могут быть выполнены как с текстовыми, так и с бинарными файлами. Для работы с бинарными
файлами используются режимы доступа "rb" (чтение бинарного файла) и "wb" (запись бинарного файла).

```python
# Чтение бинарного файла
with open("binary_file.bin", "rb") as file:
    binary_data = file.read()

# Запись бинарного файла
with open("binary_file.bin", "wb") as file:
    binary_data = b'\x00\x01\x02\x03\x04'
    file.write(binary_data)
```

## Работа с файлами в формате CSV

_CSV (comma-separated value)_ - это формат представления табличных данных (например, это могут быть данные из таблицы или
данные из базы данных).

В этом формате каждая строка файла - это строка таблицы. Несмотря на название формата, разделителем может быть не только
запятая.

И хотя у форматов с другим разделителем может быть и собственное название, например, TSV (tab separated values), тем не
менее, под форматом CSV понимают, как правило, любые разделители.

Пример файла в формате CSV (sw_data.csv):
```
hostname,vendor,model,location
sw1,Cisco,3750,London
sw2,Cisco,3850,Liverpool
sw3,Cisco,3650,Liverpool
sw4,Cisco,3650,London
```

В стандартной библиотеке Python есть модуль `csv`, который позволяет работать с файлами в CSV формате.

# Чтение

Пример чтения файла в формате CSV (файл `csv_read.py`):

```python
import csv

with open('sw_data.csv') as f:
    reader = csv.reader(f)
for row in reader:
    print(row)

# ['hostname', 'vendor', 'model', 'location']
# ['sw1', 'Cisco', '3750', 'London']
# ['sw2', 'Cisco', '3850', 'Liverpool']
# ['sw3', 'Cisco', '3650', 'Liverpool']
# ['sw4', 'Cisco', '3650', 'London']
```

В первом списке находятся названия столбцов, а в остальных соответствующие значения.

Обратите внимание, что сам csv.reader возвращает итератор:

```python
import csv

with open('sw_data.csv') as f:
     reader = csv.reader(f)
     print(reader)

# <_csv.reader object at 0x10385b050>
```

При необходимости его можно превратить в список таким образом:

```python
import csv 

with open('sw_data.csv') as f:
    reader = csv.reader(f)
    print(list(reader))

# [['hostname', 'vendor', 'model', 'location'], 
# ['sw1', 'Cisco', '3750', 'London'], 
# ['sw2', 'Cisco', '3850', 'Liverpool'], 
# ['sw3', 'Cisco', '3650', 'Liverpool'], 
# ['sw4', 'Cisco', '3650', 'London']]
``` 

Чаще всего заголовки столбцов удобней получить отдельным объектом. Это можно сделать таким образом (файл
csv_read_headers.py):

```python
import csv

with open('sw_data.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print('Headers: ', headers)
    for row in reader:
        print(row)

```

Иногда в результате обработки гораздо удобней получить словари, в которых ключи - это названия столбцов, а значения -
значения столбцов.

Для этого в модуле есть `DictReader` (файл csv_read_dict.py):

```python
import csv

with open('sw_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['hostname'], row['model'])

# {'hostname': 'sw1', 'vendor': 'Cisco', 'model': '3750', 'location': 'London, Globe Str 1 '}
# sw1 3750
# {'hostname': 'sw2', 'vendor': 'Cisco', 'model': '3850', 'location': 'Liverpool'}
# sw2 3850
# {'hostname': 'sw3', 'vendor': 'Cisco', 'model': '3650', 'location': 'Liverpool'}
# sw3 3650
# {'hostname': 'sw4', 'vendor': 'Cisco', 'model': '3650', 'location': 'London, Grobe Str 1'}
# sw4 3650
```

Примечание

До Python 3.8 возвращался отдельный тип упорядоченные словари (OrderedDict).


## Запись

Аналогичным образом с помощью модуля csv можно и записать файл в формате CSV (файл csv_write.py):

```python
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('sw_data_new.csv') as f:
    print(f.read())

# В примере выше строки из списка сначала записываются в файл, а затем содержимое файла выводится на стандартный поток
# вывода.


# hostname,vendor,model,location
# sw1,Cisco,3750,"London, Best str"
# sw2,Cisco,3850,"Liverpool, Better str"
# sw3,Cisco,3650,"Liverpool, Better str"
# sw4,Cisco,3650,"London, Best str"

```

Обратите внимание на интересную особенность: строки в последнем столбце взяты в кавычки, а остальные значения - нет.

Так получилось из-за того, что во всех строках последнего столбца есть запятая. И кавычки указывают на то, что именно
является целой строкой. Когда запятая находится в кавычках, модуль `csv` не воспринимает её как разделитель.

Иногда лучше, чтобы все строки были в кавычках. Конечно, в данном случае достаточно простой пример, но когда в строках
больше значений, то кавычки позволяют указать, где начинается и заканчивается значение.

Модуль csv позволяет управлять этим. Для того чтобы все строки записывались в CSV-файл с кавычками, надо изменить
скрипт таким образом (файл csv_write_quoting.py):

```python
import csv

data = [['hostname', 'vendor', 'model', 'location'],
['sw1', 'Cisco', '3750', 'London, Best str'],
['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)

with open('sw_data_new.csv') as f:
    print(f.read())

# "hostname","vendor","model","location"
# "sw1","Cisco","3750","London, Best str"
# "sw2","Cisco","3850","Liverpool, Better str"
# "sw3","Cisco","3650","Liverpool, Better str"
# "sw4","Cisco","3650","London, Best str"
```


Теперь все значения с кавычками. И поскольку номер модели задан как строка в изначальном списке, тут он тоже в кавычках.

Кроме метода `writerow()`, поддерживается метод `writerows()`. Ему можно передать любой итерируемый объект.

Например, предыдущий пример можно записать таким образом (файл csv_writerows.py):

```python 
import csv

data = [['hostname', 'vendor', 'model', 'location'],
['sw1', 'Cisco', '3750', 'London, Best str'],
['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)

with open('sw_data_new.csv') as f:
    print(f.read())
```

## DictWriter

С помощью DictWriter можно записать словари в формат CSV.

В целом DictWriter работает так же, как writer, но так как словари не упорядочены, надо указывать явно в каком порядке
будут идти столбцы в файле. Для этого используется параметр `fieldnames` (файл csv_write_dict.py):

```python

import csv

data = [{
'hostname': 'sw1',
'location': 'London',
'model': '3750',
'vendor': 'Cisco'
}, {
'hostname': 'sw2',
'location': 'Liverpool',
'model': '3850',
'vendor': 'Cisco'
}, {
'hostname': 'sw3',
'location': 'Liverpool',
'model': '3650',
'vendor': 'Cisco'
}, {
'hostname': 'sw4',
'location': 'London',
'model': '3650',
'vendor': 'Cisco'
}]

with open('csv_write_dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(
    f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
```


## Указание разделителя
Иногда в качестве разделителя используются другие значения. В таком случае должна быть возможность подсказать модулю,
какой именно разделитель использовать.

Например, если в файле используется разделитель `;` (файл sw_data2.csv):

```
hostname;vendor;model;location
sw1;Cisco;3750;London
sw2;Cisco;3850;Liverpool
sw3;Cisco;3650;Liverpool
sw4;Cisco;3650;London

```

Достаточно просто указать, какой разделитель используется в reader (файл csv_read_delimiter.py):

```python
import csv

with open('sw_data2.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)
```


### Работа с файлами в формате JSON

_JSON (JavaScript Object Notation)_ - это текстовый формат для хранения и обмена данными.

JSON по синтаксису очень похож на Python и достаточно удобен для восприятия.

Как и в случае с CSV, в Python есть модуль, который позволяет легко записывать и читать данные в формате JSON.

## Чтение

Файл sw_templates.json:
```json
{
  "access": [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
  ],
  "trunk": [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
  ]
}
```

Для чтения в модуле json есть два метода:

- `json.load()` - метод считывает файл в формате JSON и возвращает объекты Python
- `json.loads()` - метод считывает строку в формате JSON и возвращает объекты Python

# json.load()

Чтение файла в формате JSON в объект Python (файл json_read_load.py):

```python
import json

with open('sw_templates.json') as f:
    templates = json.load(f)

print(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))

```

# json.loads()

Считывание строки в формате JSON в объект Python (файл json_read_loads.py):

```python
import json

with open('sw_templates.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)

print(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))
```

## Запись

Запись файла в формате JSON также осуществляется достаточно легко.

Для записи информации в формате JSON в модуле json также два метода:

- `json.dump()` - метод записывает объект Python в файл в формате JSON
- `json.dumps()` - метод возвращает строку в формате JSON

# json.dumps()

Преобразование объекта в строку в формате JSON (json_write_dumps.py):

```python
import json

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.json', 'w') as f:
    f.write(json.dumps(to_json))

with open('sw_templates.json') as f:
    print(f.read())
```

Метод json.dumps подходит для ситуаций, когда надо вернуть строку в формате JSON. Например, чтобы передать ее API.

# json.dump()

Запись объекта Python в файл в формате JSON (файл json_write_dump.py):

```python
import json

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.json', 'w') as f:
    json.dump(to_json, f)

with open('sw_templates.json') as f:
    print(f.read())
```

