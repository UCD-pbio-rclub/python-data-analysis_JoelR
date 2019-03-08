# https://github.com/UCD-pbio-rclub/python_problems/wiki/Chapter-6-problem-set-2
import pandas as pd

import requests
request = requests.get("http://api.fantasy.nfl.com/v1/players/stats?statType=seasonStats&season=2010&week=1&format=json")
request
response = request.json()
response

## Answers
url = 'http://api.fantasy.nfl.com/v1/players/stats'
resp = requests.get(url)
resp

data = resp.json()
data2 = data['players']
data3 = pd.DataFrame(data2, columns=['name', 'position','teamAbbr', 'seasonPts'])

data3[data3['position']=='QB'].sort_values(by=['seasonPts'], ascending=False).head(10)




### Junqi

## Answers

# Select the first df of a list of data frames
frame = pd.read_html('https://www.thegradcafe.com/survey/index.php?q=uc+davis&t=a&o=&pp=250', header=0)[0]
print(type(frame))
frame.head()

program = frame['Program (Season)'].value_counts().head(1)
print(program)


## Kae


import requests
url = "http://www.recipepuppy.com/api/"

parameters = {"i": "nutella", "q" : "cake"}
resp = requests.get(url, params=parameters)
data = resp.json()

searchreturn = data['results']

for all in searchreturn:
    if 'egg' not in all['ingredients']:
        print(all['title'] + " : " + all['href'])


rec = [(all['title'] + " : " + all['href']) for all in searchreturn if 'egg' not in all['ingredients']]
