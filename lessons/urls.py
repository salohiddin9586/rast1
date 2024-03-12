from django.urls import path
from lessons.views import lesson_list, create_lesson, update_lesson, patrial_update_lesson, delete_lesson

urlpatterns = [
    path('lessons/', lesson_list),
    path('lessons/<int:pk>/', lesson_list),
    path('create/', create_lesson),
    path('update/<int:pk>/', update_lesson),
    path('pr-update/<int:pk>/', patrial_update_lesson),
    path('delete/<int:pk>/', delete_lesson),
]


# from lessons.views import fruits, create_fruit, detail_fruits
# urlpatterns = [
#     path('fruits/', fruits),
#     path('fruits/<int:pk>', detail_fruits),
#     path('fruits/create/', create_fruit),
# ]

