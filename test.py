# -*- coding: utf-8 -*-
from django.conf import settings
host = 'https://paas.blueking.com'
import requests
import json

url = host + '/login/accounts/is_login/'
data = {"bk_token": "JbFZhq8uiAD3VeujAqHcj-0owF-hN1uU1kSdOlfu8O0"}
headers = {'Accept': 'application/json','Content-Type': 'application/json'}

result = requests.get(url, headers=headers, params=data,verify=False)
if result.status_code == 200:
    content = json.loads(result.content)
    print(content)
else:
    print(result)
# app_url= host + '/api/c/compapi/v2/cc/search_business/'
# print(app_url)
# user_url = host + '/api/c/compapi/v2/bk_login/get_user/'
#
# import json
# # 修改模块属性
# modify_module_properties = 'http://aospaas.travelsky.com/api/c/compapi/cc/modify_module_properties/'
# from settings import APP_ID
#
# data = {"bk_app_code": 'liupeng',
#         "bk_token":'a3S9jNPQEq7vEONoNGKLhvZXvMD8FmIS',
#         "bk_app_secret":'bce161ad-188b-4184-8232-a6e97de0cae5'}
# data = json.dumps(data)
# headers = {'Accept': 'application/json','Content-Type': 'application/json'}
# result = requests.post(app_url, headers=headers, data=data)
#
# if result.status_code == 200:
#     content = json.loads(result.content)
#     print(content)


