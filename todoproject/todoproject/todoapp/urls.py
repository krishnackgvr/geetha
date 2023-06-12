from django.conf.urls.static import static
from django.urls  import path

from todoapp import views
from todoproject import settings

urlpatterns=[
    path('',views.add,name='add'),
   # path('details/',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listlook/',views.TaskListView.as_view(),name='listlook'),
    path('detaillook/<int:pk>/',views.TaskDetailView.as_view(),name='detaillook'),
    path('updatelook/<int:pk>/',views.TaskUpdateView.as_view(),name='updatelook'),
    path('deletelook/<int:pk>/', views.TaskDeleteView.as_view(),name='deletelook')
]
if settings.DEBUG:
     urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)