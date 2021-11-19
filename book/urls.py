from django.urls import path, include

from book.views import home, AuthorDetailView, AuthorListView

urlpatterns = [
        # path('', home, name='home'), 
        path('', AuthorListView.as_view(), name='author-list'),
        path('author/<int:pk><str:slug>/',
            AuthorDetailView.as_view(),name='author-pk-slug-detail')
]
