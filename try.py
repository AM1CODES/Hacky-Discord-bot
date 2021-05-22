import requests

r = requests.get('https://hackathons.hackclub.com/api/events/upcoming')
result = r.json()
for i in range(10):
    print(result[i]['name'])

print(len(result))

result1 = {}
for i in range(0,len(result)):
    result1.update(result[i])
    
print(result1)



