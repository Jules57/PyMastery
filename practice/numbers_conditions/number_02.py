"""Спросить пользователя возраст, пол и имя. Для всех младше 15 мы пишем, что рекомендуем теннис, для парней старше 15
   рекомендуем футбол, для девушек баскетбол, но если в имени есть буква 'c' или 't', печатаем что мы не рекомендуем
   заниматься спортом."""

age = 6
name = 'baby-hank'
gender = 'male'

if 'c' in name or 't' in name:
    print('No sports. Sorry. Stay fat.')
elif 0 < age < 15:
    print('Tennis is a great choice')
elif age >= 15 and gender == 'male':
    print('Soccer is a great choice')
elif age >= 15 and gender == 'female':
    print('Basketball is a great choice')
else:
    print('Have a good day.')
