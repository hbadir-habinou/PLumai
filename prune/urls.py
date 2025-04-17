from django.urls import path
from prune_app.views import index, a_propos, contact, nos_services, login, signin,prediction_plum

urlpatterns = [
    path('', index, name='index'),
    path('a-propos/', a_propos, name='a_propos'),
    path('contact/', contact, name='contact'),
    path('nos-services/', nos_services, name='nos_services'),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('prediction_plum/', prediction_plum, name='prediction_plum'),
]
