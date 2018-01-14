import json
import requests
headers={'userkey':'4f17f9f7a7'}

url='http://www.lewei50.com/api/V1/gateway/updatelog/01'
'''
payload={'Message':'it is ok'}
r=requests.post(url,json.dumps(payload),headers=headers)
print (r.text)
'''
url='http://www.lewei50.com/api/V1/gateway/UpdateSensors/01'
payload=[{'Name':'000001-VR','Value':'100'}]
r=requests.post(url,json.dumps(payload),headers=headers)
print (r.text)

