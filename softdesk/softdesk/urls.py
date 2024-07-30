from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import UserViewset
from project.views import ProjectViewset, IssueViewset, CommentViewset

router = routers.SimpleRouter()
router.register("users", UserViewset)
router.register("projects", ProjectViewset)

projects_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
projects_router.register("issues", IssueViewset, "issues")

issues_router = routers.NestedSimpleRouter(projects_router, "issues", lookup="issue")
issues_router.register("comments", CommentViewset, "comments")

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path("api/", include(projects_router.urls)),
    path("api/", include(issues_router.urls)),
]
