from django.urls import path, re_path
from . import views

# path(path / urls / kwargs / name)
# re_path regular expression
# path( r'^([0-9]+)/$'
# match path 1-9 do not include anything after
# another way with path to get a specific index and show it

# path('<int:cat_id>/', views.show, name='show
# path('<int:cat_id>/edit/', views.edit_cat, name='edit_cat'),
# path('<int:cat_id>/destroy/', views.delete_cat, name='delete_cat'),

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^([0-9]+)/$', views.show, name='show'),
    path('<int:cat_id>/', views.show, name='show'),
    path('post_cat/', views.post_cat, name='post_cat'),
    path('user/<user_name>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('like_cat/', views.like_cat, name='like_cat'),
    path('<int:cat_id>/edit/', views.edit_cat, name='edit_cat'),
    path('<int:cat_id>/destroy/', views.delete_cat, name='delete_cat'),
    path('<int:cat_id>/toy/create/', views.create_toy, name='create_toy'),
    path('toy/<int:toy_id>/', views.show_toy, name='show_toy'),
    path('api/', views.api, name='api'),
]
