"""
URL configuration for softdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from authentication.views import UserViewset
from project.views import ProjectViewset, IssueViewset, CommentViewset
from contributor.views import ContributorViewset

router = routers.SimpleRouter()

router.register(prefix="users", viewset=UserViewset, basename="users")
router.register(prefix="projects", viewset=ProjectViewset, basename="projects")
router.register(prefix="issues", viewset=IssueViewset, basename="issues")
router.register(prefix="comments", viewset=CommentViewset, basename="comments")
router.register(prefix="contributors", viewset=ContributorViewset, basename="contributors")

urlpatterns = [
    path("api/", include(router.urls))
]
