from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('index/', WomenMain.as_view(), name='index'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('addfilm/', AddFilm.as_view(), name='add_film'),
    path('article/<slug:slug_name>/', ShowPost.as_view(), name='article'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(),
         name='show_category'),
    path('about_us/', AboutView.as_view(), name='about_site'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cv/', cv_view, name='cv')
]
