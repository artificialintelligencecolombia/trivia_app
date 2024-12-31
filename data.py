import requests

url = 'https://opentdb.com/api.php'
parameters = {'amount':10, 'type':'boolean'}

response = requests.get(url, params=parameters)
response.raise_for_status() 
question_data = response.json()['results']

# Test
print(question_data)
print(type(question_data))