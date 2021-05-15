import requests

list_of_heroes = ['Hulk', 'Captain America', 'Thanos']
TOKEN = 2619421814940190

#Функция для определения id какого-либо героя
def get_superhero_id(name):
    resp = requests.get(f'https://superheroapi.com/api/{TOKEN}/search/{name}').json()['results']
    for hero in resp:
      return hero['id']

# Функция для получения интеллекта героя
def get_intelligence(name):
    hero_id = get_superhero_id(name)
    resp = requests.get(f'https://superheroapi.com/api/{TOKEN}/{hero_id}/powerstats').json()['intelligence']
    return {name:resp}

# Функция для определения самого умного
def find_the_smartest_char(list):
    # инициализируем переменные
    smartest_hero_int = 0
    smartest_hero_name = 'abc'
    #итеррируеимся по списку героев
    for i in list:
        # т.к. данные об интеллекте сохранены для получения значения используем (i)[i]
        if int(get_intelligence(i)[i]) > smartest_hero_int:
            smartest_hero_int = int(get_intelligence(i)[i])
            smartest_hero_name = i
    return f'{smartest_hero_name} самый умный герой с величиной интеллекта - {smartest_hero_int}'

print(find_the_smartest_char(list_of_heroes))
