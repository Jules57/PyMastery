
1. Как работает словарь в Python?
2. Элемент в словаре имеет две части. Как они называются?
3. Какая часть элемента словаря должна быть неизменяемой?
4. Предположим, что `'start':1472 `является элементом словаря. Что является ключом? И что является значением?
5. Предположим, что создан словарь с именем `employee`. Что делает приведенная ниже инструкция?
```python
employee['id'] = 54321
```
6. Что покажет приведенный ниже фрагмент кода?
```python
stuff = {1:'chair', 2:'table', 3:'sofa'} 
print(stuff[3])
```
7. Как определить, существует ли пара `ключ : значение` в словаре?
8. Предположим, что существует словарь `inventory`. Что делает приведенная ниже инструкция?
```python
del inventory[654]
```
9. Что покажет приведенный ниже фрагмент кода? 
```python
stuff = {1:'table', 2:'chair', 3:'sofa'}
print(len(stuff))

```
10. Что покажет приведенный ниже фрагмент кода?
```python
stuff = {1:'table', 2:'chair', 3:'sofa'}
for key in stuff:
    print(key)
```
11. В чем разница между словарными методами `pop()` и `popitem()`?
12. Что возвращает метод items()?
13. Что возвращает метод keys()?
14. Что возвращает метод values () ?
15. Предположим, что существует следующий список:
```python
names = ['Chris', 'Kevin', 'Joan', 'Jim']
```
Напишите инструкцию с использованием включения в словарь для создания словаря, в котором каждый элемент содержит имя из
списка names в качестве ключа и длину этого имени в качестве значения.

16. Предположим, что существует следующий словарь:
```python
phonebook = {'Chris':'919-555-1111', 'Kevin':'828-555-2222', 'Joan':'704-555-3333', 'Jim':'919-555-3333'}
```
Напишите инструкцию с использованием включения в словарь для создания второго словаря, содержащего элементы телефонной 
книги `phonebook`, которые имеют значения, начинающееся с '919'.
