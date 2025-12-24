from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('create/', views.create_issue, name='create_issue'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.history, name='history'),
    path('filter_search/', views.filter_search, name='filter_search'),

    path('issue/start/<int:issue_id>/', views.start_issue, name='start_issue'),
    path('issue/close/<int:issue_id>/', views.close_issue, name='close_issue'),

    path(
        'issue/<int:issue_id>/status/<str:new_status>/',
        views.update_issue_status,
        name='update_issue_status'
    ),

    path(
    'issue/<int:issue_id>/',
    views.view_issue,
    name='view_issue'
),



    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
