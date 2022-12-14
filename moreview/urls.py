"""moreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from review.views import (
    ReviewCreateView,
    # ReviewCreate
)

urlpatterns = [
    path("base", TemplateView.as_view(template_name="base.html")),
<<<<<<< HEAD
    path("admin/", admin.site.urls),

    #app: movie
    path("", MovieListView.as_view(), name="movie_list"),
    path("movies/create", MovieCreateView.as_view(), name="movie_create_form"),
    path("movies/<int:pk>", MovieDetailView.as_view(), name="movie_detail"),
    path("movies/<int:pk>/edit", MovieEditView.as_view(), name="movie_edit"),
    path("movies/<int:pk>/delete", MovieDeleteView.as_view(), name="movie_delete"),

    #app: review
    path("reviews/create", ReviewCreateView.as_view(), name="review_create"),
=======
    path("", include("users.urls")),
    path("", include("movie.urls")),
    path("", include("review.urls")),
    # path("admin/", admin.site.urls),
>>>>>>> 93a16b8716ae30c4eaadc8d136f789c960e7a853
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
