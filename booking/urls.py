from . import views
from django.conf.urls import url
from django.urls import path
from .views import GeneratePdf
urlpatterns = [
	path('ticketbook/', views.ticketbook),
    path('seat/', views.seat),
    path('show/', views.show),
    path('get/', GeneratePdf.as_view()),
    path('cancel_booking/',views.cancel_booking),
    path('confirme/', views.confirme,name="confirme"),
    path('<str:param1>/<str:param2>/',views.remove,name="remove"),
    path('<str:key>/',views.showbus,name="showbus"),

        
]
