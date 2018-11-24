# -*- coding: utf-8 -*-
from django.conf import settings
host = 'https://paas-poc.o.qcloud.com'
import requests
app_url= host + '/api/c/compapi/v2/cc/search_business/'
print(app_url)
# 修改模块属性
modify_module_properties = 'http://aospaas.travelsky.com/api/c/compapi/cc/modify_module_properties/'
from settings import APP_ID
{'bk_app_code':APP_ID}

result = requests.post(app_url,
                       headers={'Accept': 'application/json',
                                'Content-Type': 'application/json', },
                       data=None)



