import json

json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'

x = json.loads(json_str)

for i in x:
    print(i)

json_str2 = json.dumps(x)

print(json_str2)













