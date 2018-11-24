# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from account.accounts import Account
from django.conf import settings

def home(request):
    """
    首页
    """
    #return render_mako_context(request, '/home_application/home.html')
    account = Account()

    is_ok,resp= account.get_bk_user_info(settings.APP_TOKEN)
    # return account.logout(request)
    print(resp)
    return render_mako_context(request, '/home_application/index.html',resp)

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
