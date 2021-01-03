from django.conf.urls import url

from user import views

urlpatterns=[
    url(r"^login/$",views.login),
    url(r"^info/",views.userInfo),
    url(r"^logout/",views.logOut),

]