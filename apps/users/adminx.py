import xadmin
from .models import BannerInfo,EmailVerifyCode
from xadmin import views

#配置xadmin主题,注册的时候要用到专用的view去注册
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True

class BannerInfoXadmin(object):
    list_display = ['image','url','add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']

class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']

xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
#注册主题类
xadmin.site.register(views.BaseAdminView,BaseXadminSetting)
#注册全局样式的类
