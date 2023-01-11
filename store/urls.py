from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.login, name='login'),
    path('pos', views.pos, name='pos'),
    path('pos/p_selected', views.selected, name='selected'),
    path('pos/p_selected_delete', views.deleted, name='delete'),
    path('pos/<int:p_id>', views.selected, name='selected'),
    # re_path('pos/search/<str:s>', views.search, name='search'),
    path('admin', RedirectView.as_view(url="/admin"), name="admin"),
]
