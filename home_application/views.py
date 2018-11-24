# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from account.accounts import Account
from django.conf import settings
from account.decorators import login_exempt
import requests

@login_exempt
def home(request):
    """
    首页
    """
    #bk_token = request.COOKIES.get(settings.BK_COOKIE_NAME, None)


    #return render_mako_context(request, '/home_application/home.html')
    #account = Account()
    #user_info = account.get_bk_user_info(bk_token)

    return render_mako_context(request, '/home_application/index.html')

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
