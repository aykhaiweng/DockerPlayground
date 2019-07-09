from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.views import View


class DockerApp1View(View):
    http_method_names = ['get']

    def get(self, request):
        """
        This is DockerApp1's example View

        Khai, 25.06.2019
        """
        print("LOL?")
        return HttpResponse("DockerApp1 Greets You")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dockerapp1/views/test/', View.as_view())
]
