import requests
import json
url= 'http://127.0.0.1:7788'
data = {
    'files':open('22.jpg','rb')
}
r = requests.post(url,data=open('22.jpg','rb'))
print(r.encoding)
print(r.status_code)
s= json.loads(r.text)
print(s)




# import requests
# import json
#
r=requests.post('http://127.0.0.1:7788',data=open('22.jpg','rb'))
code=json.loads(r.text)['code']
print(code)