from django.urls import path
from to_do_list.views import (
    index,
    status_change,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "to_do_list"

urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task-list"),
    path("task_list/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task_list/change_completed/<int:pk>/", status_change, name="status_change"
    ),
    path(
        "task_list/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task_list/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path("tag_list/", TagListView.as_view(), name="tag-list"),
    path("tag_list/create/", TagCreateView.as_view(), name="tag-create"),
    path(
        "tag_list/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tag_list/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
]
