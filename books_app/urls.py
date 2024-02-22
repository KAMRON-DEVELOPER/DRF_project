from django.urls import path
from .views import BookListApiView, BookRetrieveAPIView, BookRetrieveDestroyAPIView
from .views import BookRetrieveUpdateAPIView, BookRetrieveUpdateDestroyAPIView, BookListAPIView
from .views import BookCreateAPIView, BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView


urlpatterns = [
    path('', BookListApiView.as_view()),
    path('<int:pk>/detail/', BookRetrieveAPIView.as_view()),
    path('<int:pk>/detail_delete/', BookRetrieveDestroyAPIView.as_view()),
    path('<int:pk>/detail_update/', BookRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/detail_update_delete/', BookRetrieveUpdateDestroyAPIView.as_view()),
    
    path('APIView/', BookListAPIView.as_view()),
    path('APIView/create/', BookCreateAPIView.as_view()),
    path('APIView/<int:pk>/', BookDetailAPIView.as_view()),
    path('APIView/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    path('APIView/<int:pk>/update/', BookUpdateAPIView.as_view()),
]




