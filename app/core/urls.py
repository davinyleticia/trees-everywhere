from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.user_login, name='user_login'),
    path('planted-trees/', views.planted_trees, name='planted_trees'),
    path('planted-trees/<int:tree_id>/', views.planted_tree_detail, name='planted_tree_detail'),
    path('add-planted-tree/', views.add_planted_tree, name='add_planted_tree'),
    path('account-trees/', views.account_trees, name='account_trees'),
    path('add-tree/', views.add_tree, name='add_tree'),
    path('add-account/', views.add_account, name='add_account'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('api/planted-trees/', views.PlantedTreesListView.as_view(), name='planted-trees-list'),
    path('api/login/', views.LoginView.as_view(), name='login')
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
