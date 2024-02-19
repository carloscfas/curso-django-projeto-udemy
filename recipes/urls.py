from django.urls import path

from recipes.views import home


# cliente pede    servidor responde 
# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST

#def sobre(request):
#    return HttpResponse('Sobre')
    # return HTTP Response

urlpatterns = [
    path('', home), # Home
]
