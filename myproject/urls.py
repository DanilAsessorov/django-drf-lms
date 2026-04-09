from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Django DRF LMS Project</h1>
        <p>Добро пожаловать в API системы управления обучением!</p>
        <h2>Доступные эндпоинты:</h2>
        <ul>
            <li><a href="/admin/">/admin/</a> - Админ-панель</li>
            <li><a href="/api/courses/">/api/courses/</a> - Список курсов</li>
            <li><a href="/api/lessons/">/api/lessons/</a> - Список уроков</li>
        </ul>
    """)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('lms.urls', namespace='lms')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)