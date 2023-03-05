from django .urls import path
from.import views

app_name = 'conversation'


urlpatterns = [
    path('inbox/', views.inbox, name = 'inbox'),
    path('<int:pk>/', views.detailMessage, name = 'detailMessage'),
    path('new_conversation/<int:item_pk>', views.new_conversation, name = 'new_conversation')
]