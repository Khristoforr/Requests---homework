import requests

def get_questions_about_python():
    url = 'https://api.stackexchange.com/2.2/questions?pagesize=100&' \
          'fromdate=1620864000&todate=1621123200&order=desc&sort=activity&tagged=python&site=stackoverflow'
    resp = requests.get(url).json()
    x = len(resp['items'])
    for i in range(x):
        print(resp['items'][i]['title'], resp['items'][i]['link'])

get_questions_about_python()