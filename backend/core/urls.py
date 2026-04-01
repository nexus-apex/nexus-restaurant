from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('menuitems/', views.menuitem_list, name='menuitem_list'),
    path('menuitems/create/', views.menuitem_create, name='menuitem_create'),
    path('menuitems/<int:pk>/edit/', views.menuitem_edit, name='menuitem_edit'),
    path('menuitems/<int:pk>/delete/', views.menuitem_delete, name='menuitem_delete'),
    path('tableorders/', views.tableorder_list, name='tableorder_list'),
    path('tableorders/create/', views.tableorder_create, name='tableorder_create'),
    path('tableorders/<int:pk>/edit/', views.tableorder_edit, name='tableorder_edit'),
    path('tableorders/<int:pk>/delete/', views.tableorder_delete, name='tableorder_delete'),
    path('diningtables/', views.diningtable_list, name='diningtable_list'),
    path('diningtables/create/', views.diningtable_create, name='diningtable_create'),
    path('diningtables/<int:pk>/edit/', views.diningtable_edit, name='diningtable_edit'),
    path('diningtables/<int:pk>/delete/', views.diningtable_delete, name='diningtable_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
