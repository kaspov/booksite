from django.urls import path, include

from book.views import ( home, AuthorDetailView, 
                        AuthorListView, ReaderListView )

urlpatterns = [
        path('reader/', ReaderListView.as_view(), name='reader-list'), 
        path('author/<int:pk>-<str:slug>/',AuthorDetailView.as_view(),name='author-pk-slug-detail'), 
        path('reader/<int:pk>-<str:slug>/',AuthorDetailView.as_view(),name='reader-pk-slug-detail'), 
        path('', AuthorListView.as_view(), name='author-list'),
]
