import requests;
import types;

url = 'http://localhost:8080/api/v0/events';
starttime = 1675159200;
delta = 172800;
user = 'v.ivanov';
json = {
            "start": starttime,
            "end": starttime+delta,
            "user": user,
            "team": "Team1",
            "role": "secondary",
        };

r = requests.post(url,json=json);


rep = requests.get(url);
print(rep.text);

