# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.request import Request

# from lessons.seriallizers import FruitSerializer

# fruits_list = [
#     {"id": 1, "name": "apple", "price": 83},
#     {"id": 2, "name": "banana", "price": 57},
#     {"id": 3, "name": "orange", "price": 94},
# ]
#
#
# @api_view(http_method_names=["GET"])
# def fruits(request: Request):
#     return Response(fruits_list, status=200)
#
#
# @api_view(http_method_names=['POST'])
# def create_fruit(request: Request):
#     data = request.data
#     fruits_list.append(data)
#     return Response(fruits_list, status=201)
#
#
# @api_view(http_method_names=["GET"])
# def detail_fruits(request: Request, pk: int):
#     fruit = [i for i in fruits_list if i['id'] == pk]
#     return Response(fruit, status=200)

import json
import requests
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from lessons.models import Lesson
from lessons.seriallizers import LessonSerializer


@api_view(http_method_names=['GET'])
def lesson_list(request: Request, pk=None):
    if pk:
        data = Lesson.objects.get(id=pk)
        serializer = LessonSerializer(instance=data)
        return Response(serializer.data, status=HTTP_200_OK)

    data = Lesson.objects.all()

    serializer = LessonSerializer(instance=data, many=True)

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(http_method_names=['POST'])
def create_lesson(request: Request):
    title, subject, plan = request.data['title'], request.data['subject'], request.data['plan']
    data = Lesson.objects.create(title=title, subject=subject, plan=plan)
    serializer = LessonSerializer(instance=data)

    return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(http_method_names=['PUT'])
def update_lesson(request: Request, pk):
    title, subject, plan = request.data['title'], request.data['subject'], request.data['plan']
    data = Lesson.objects.get(id=pk)
    data.title = title
    data.subject = subject
    data.plan = plan
    data.save()

    serializer = LessonSerializer(instance=data)

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(http_method_names=['PATCH'])
def patrial_update_lesson(request: Request, pk):
    try:
        title = request.data['title'],
    except KeyError:
        title =None

    try:
        subject = request.data['subject'],
    except KeyError:
        subject = None

    try:
        plan = request.data['plan']
    except KeyError:
        plan = None

        data = Lesson.objects.get(id=pk)

    if title:
        data.title = title
        data.save()

    if subject is not None:
        data.subject = subject
        data.save()

    if plan:
        data.plan = plan
        data.save()

    serializer = LessonSerializer(instance=data)

    return Response(serializer.data, status=HTTP_200_OK)

@api_view(http_method_names=['DELETE'])
def delete_lesson(request: Request, pk):
    lesson = Lesson.objects.get(id=pk)
    lesson.delete()

    data = Lesson.objects.get(id=pk)
    serializer = LessonSerializer(instance=data, many=True)

    return Response(serializer.data,status=HTTP_200_OK)


def template_lesson_list(request: Request):
    response = requests.get("http://localhost:8000/api/v1/lessons/")
    print(response.text)

    lessons = json.loads(response.text)
    # data = json.dumps(lessons)

    context = {
        "lessons": lessons
    }
    return render(request,'index.html',context)




