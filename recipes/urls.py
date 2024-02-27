from django.urls import path

from . import views


# cliente pede    servidor responde 
# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST

#def sobre(request):
#    return HttpResponse('Sobre')
    # return HTTP Response

urlpatterns = [
    path('', views.home), # Home
    path('recipes/<int:id>/', views.recipe),
]
