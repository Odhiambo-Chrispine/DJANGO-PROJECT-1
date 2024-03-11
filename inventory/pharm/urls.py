from pharm import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('admin',views.admin,name='admin'),
    path('navbar',views.navbar,name='navbar'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('items',views.items,name='items'),
    path('add',views.add,name='add'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('others',views.others,name='others'),
    path('issue',views.issue,name='issue'),
    path('detail/<str:pk>/',views.detail,name='detail'),
    path('issue_item/<str:pk>/',views.issue_item,name='issue_item'),
    path('receive_item/<str:pk>/',views.receive_item,name='receive_item'),
    path('reorder_level/<str:pk>/',views.reorder_level,name='reorder_level'),
]