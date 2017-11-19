from django.conf.urls import url
from api import views as api_views

user_list = api_views.UserList.as_view({
    'get': 'list',
    'post': 'create'
})

city_list = api_views.CityList.as_view({
    'get': 'list',
    'post': 'create'
})

province_list = api_views.ProvinceList.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    url(r'^users/$', user_list, name='user-list'),
    url(r'^cities/$', city_list, name='city-list'),
    url(r'^provinces/$', province_list, name='province-list')
]
