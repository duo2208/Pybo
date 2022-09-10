from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    path('', base_views.qna_list, name='qna_list'),
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('pybo/', include('pybo.urls')),
]

handler404 = 'common.views.page_not_found'
handler500 = 'common.views.server_error'