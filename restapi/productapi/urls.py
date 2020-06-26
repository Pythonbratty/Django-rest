from django.urls import path
from .views import MemberListView
from .views import PeriodListView




urlpatterns= [

    path("api/Members", MemberListView.as_view()),
    path("api/Periods", PeriodListView.as_view())


    ]