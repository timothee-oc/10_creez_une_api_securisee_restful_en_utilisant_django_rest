from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers
from authentication.views import UserViewset
from project.views import ProjectViewset, IssueViewset, CommentViewset

router = routers.SimpleRouter()
router.register(prefix="users", viewset=UserViewset, basename="users")
router.register(prefix="projects", viewset=ProjectViewset, basename="projects")

projects_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
projects_router.register(prefix="issues", viewset=IssueViewset, basename="project-issues")

issues_router = routers.NestedSimpleRouter(projects_router, "issues", lookup="issue")
issues_router.register(prefix="comments", viewset=CommentViewset, basename="issue-comments")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/", include(projects_router.urls)),
    path("api/", include(issues_router.urls)),
]
