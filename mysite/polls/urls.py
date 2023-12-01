from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    #path('', views.name, name='name'),
    path('', views.index, name='index'), # name을 하는 이유는 더 오류 났을때 쉽게 찾으려고
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
] # polls/를 없애는 이유는 앞에 url에서 추가했기 때문이다.