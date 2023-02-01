import requests;

call = input('call= ')
email = input('email= ')
slack = input('slack= ')
sms = input('sms= ')
full_name = input('full_name= ')
photo_url = input('photo_url= ')
time_zone = input('time_zone= ')


def create_user_oncall(call, email, slack, sms, full_name, photo_url, time_zone):
   requests.post('http://localhost:8080/api/v0/users', json={'name': slack},
                      headers={'content-type': 'application/json; charset = utf-8', 'Expect': ''});
   requests.put('http://localhost:8080/api/v0/users/'+slack,
                       json={"contacts":
                        {
                            "call": call,
                            "email": email,
                            "slack": slack,
                            "sms": sms
                        },
                        "full_name": full_name,
                        "photo_url": photo_url,
                        "time_zone": time_zone,
                        "active": 1});


create_user_oncall(call, email, slack, sms, full_name, photo_url, time_zone)

req_for_get_users_with_changes = requests.get('http://localhost:8080/api/v0/users');
print(req_for_get_users_with_changes.text)
