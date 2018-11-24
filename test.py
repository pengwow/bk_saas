# -*- coding: utf-8 -*-
from django.conf import settings
host = 'https://paas-poc.o.qcloud.com'
import requests
app_url= host + '/api/c/compapi/v2/cc/search_business/'
print(app_url)
user_url = host + '/api/c/compapi/v2/bk_login/get_user/'

import json
# 修改模块属性
modify_module_properties = 'http://aospaas.travelsky.com/api/c/compapi/cc/modify_module_properties/'
from settings import APP_ID

data = {"bk_app_code": 'liupeng',
        "bk_token":'rF5XaVk3SaqZ3n1L_aek_3YtM2ViYR9IQeW1I5Wdrng',
        "bk_app_secret":'b0850347-93ec-4d92-84db-7637ce6d6056'}
data = json.dumps(data)
result = requests.post(user_url,
                       headers={'Accept': 'application/json',
                                'Content-Type': 'application/json', },
                       data=data)

if result.status_code == 200:
    content = json.loads(result.content)
    print(content)


