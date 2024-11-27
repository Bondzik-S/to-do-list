from django.urls import path

from to_do_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_task_status,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/create/", TaskCreateView.as_view(), name='task_create'),
    path("task/edit/<int:pk>/", TaskUpdateView.as_view(), name='task_edit'),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name='task_delete'),
    path('task/toggle/<int:pk>/', toggle_task_status, name='toggle_task_status'),
    path("tags/", TagListView.as_view(), name='tag_list'),
    path("tag/create/", TagCreateView.as_view(), name='tag_create'),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name='tag_update'),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name='tag_delete'),
    ]


app_name = "to_do_list"