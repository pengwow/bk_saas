# -*- coding: utf-8 -*-
from django.conf import settings
# 平台验证用户登录态接口
BK_LOGIN_VERIFY_URL = "%s/login/accounts/is_login/" % getattr(settings, 'BK_PAAS_INNER_HOST', settings.BK_PAAS_HOST)
# 平台获取用户信息接口
BK_GET_USER_INFO_URL = "%s/login/accounts/get_user/" % getattr(settings, 'BK_PAAS_INNER_HOST',
                                                               settings.BK_PAAS_HOST)
from account.http import http_get
param = {'bk_token': 'b0850347-93ec-4d92-84db-7637ce6d6056'}
result, resp = http_get(BK_GET_USER_INFO_URL, param)
print(result, resp )