# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
import requests
import json

def home(request):
    """
    首页
    """
    try:
        bk_token = request.COOKIES.get('bk_token', None)
        if not bk_token:
            return render_mako_context(request, '/home_application/dev_guide.html')
        host = 'https://paas-poc.o.qcloud.com'

        app_url = host + '/api/c/compapi/v2/cc/search_business/'

        data = {"bk_app_code": 'liupeng',
                "bk_token": bk_token,
                "bk_app_secret": 'b0850347-93ec-4d92-84db-7637ce6d6056'}
        data = json.dumps(data)
        result = requests.post(app_url,
                               headers={'Accept': 'application/json',
                                        'Content-Type': 'application/json', },
                               data=data)

        if result.status_code == 200:
            content = json.loads(result.content)
            content = content.get('data')
            print(content.get('data'))
    except:
        print('aaaaaaaaaaa')
    return render_mako_context(request, '/home_application/index.html',content)


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
