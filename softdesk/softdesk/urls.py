from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers
from authentication.views import UserViewset
from project.views import ProjectViewset, IssueViewset, CommentViewset
from contributor.views import ContributorViewset

router = routers.SimpleRouter()
router.register(prefix="users", viewset=UserViewset, basename="users")
router.register(prefix="projects", viewset=ProjectViewset, basename="projects")
router.register(prefix="contributors", viewset=ContributorViewset, basename="contributors")

projects_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
projects_router.register(prefix="issues", viewset=IssueViewset, basename="project-issues")

issues_router = routers.NestedSimpleRouter(projects_router, "issues", lookup="issue")
issues_router.register(prefix="comments", viewset=CommentViewset, basename="issue-comments")

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path("api/", include(projects_router.urls)),
    path("api/", include(issues_router.urls)),
]
