# -*- coding: utf-8 -*-
from django.conf import settings
host = 'https://paas-poc.o.qcloud.com'
import requests
app_url= host + '/api/c/compapi/v2/cc/search_business/'
print(app_url)
# 修改模块属性
modify_module_properties = 'http://aospaas.travelsky.com/api/c/compapi/cc/modify_module_properties/'
from settings import APP_ID

data = {"bk_app_code": 'liupeng',
        "bk_username":'liupeng',
        "bk_app_secret": 'b0850347-93ec-4d92-84db-7637ce6d6056'}

result = requests.post(app_url,
                       headers={'Accept': 'application/json',
                                'Content-Type': 'application/json', },
                       data=data)
import json
if result.status_code == 200:
    content = json.loads(result.content)

    print(content)


