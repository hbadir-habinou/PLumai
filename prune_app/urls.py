from django.urls import path
from prune_app.views import index, login, signin, a_propos, contact, nos_services,prediction_plum

urlpatterns = [
    path('', index, name='index'),              # Page d'accueil
    path('login/', login, name='login'),        # Page de connexion
    path('signin/', signin, name='signin'),     # Page d'inscription
    path('a-propos/', a_propos, name='a_propos'),  # Page À propos
    path('contact/', contact, name='contact'),  # Page Contact
    path('nos-services/', nos_services, name='nos_services'),  # Page Nos services
    path('prediction_plum/', prediction_plum, name='prediction_plum'),  # Page pour les predictions
]