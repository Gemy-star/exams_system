from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import models
from users.models import User
from django.core import serializers


def create_exam(request):
    context = {"questions": models.Question.objects.all(), "exams": models.Exam.objects.all(),
               "cats": models.Category.objects.all()}
    if request.method == 'GET':
        return render(request, 'exam/create_exam.html', context=context)
    elif request.method == 'POST' or request.is_ajax:
        exam_info = models.Exam()
        exam_info.name = request.POST.get('name')
        cat_id = request.POST.get('cat_id')
        cat_obj = models.Category.objects.get(pk=cat_id)
        exam_info.cat_name = cat_obj
        questions = request.POST.getlist('questions[]')
        exam_info.save()
        for question in questions:
            q = models.Question.objects.get(pk=question)
            exam_info.ques.add(q)
        return JsonResponse({"data": "1"})
    else:
        return render(request, 'exam/create_exam.html', context=context)


def create_question(request):
    context = {"questions": models.Question.objects.all(),
               "cats": models.Category.objects.all()}
    if request.method == 'GET':
        return render(request, 'exam/create_question.html', context=context)
    elif request.method == 'POST' or request.is_ajax:
        question_info = models.Question()
        question_info.question = request.POST.get('question_name')
        cat = request.POST.get('cat_id')
        cat_obj = models.Category.objects.get(pk=cat)
        question_info.cat_name = cat_obj
        marks = request.POST.get('marks')
        question_info.marks = marks
        option1 = request.POST.get('option1')
        question_info.option1 = option1
        option2 = request.POST.get('option2')
        question_info.option2 = option2
        option3 = request.POST.get('option3')
        question_info.option3 = option3
        option4 = request.POST.get('option4')
        question_info.option4 = option4
        answer = request.POST.get('answer')
        question_info.answer = answer
        question_info.save()
        return JsonResponse({"data": "1"})
    else:
        return render(request, 'exam/create_question.html', context=context)


def cat_exam_list(request, pk):
    category = models.Category.objects.get(pk=pk)
    exams = models.Exam.objects.filter(cat_name=category)
    context = {"cat": category, "exams": exams}
    return render(request, 'exam/exam_cat_list.html', context=context)


def exam_detail(request, pk):
    marks = 0
    exam_info_obj = models.Exam.objects.get(pk=pk)
    exam_questions = exam_info_obj.ques.all()
    context = {"exam": exam_info_obj, "questions": exam_questions}
    if request.method == 'GET':
        return render(request, 'exam/exam_detail.html', context=context)
    elif request.method == 'POST' or request.is_ajax:
        answers = request.POST.getlist('answers[]')
        for index, question in enumerate(exam_questions):
            if answers[index] == question.answer:
                marks += question.marks
        user = User.objects.get(pk=request.user.pk)
        result = models.FinalResult(user=user, exam=exam_info_obj, total=marks)
        result.save()
        if result.pk:
            return JsonResponse({"data": "1"})
        else:
            return JsonResponse({"data": "-1"})
    elif request.method == 'GET':
        return render(request, 'exam/exam_detail.html', context=context)
    else:
        return render(request, 'exam/exam_detail.html', context=context)


def get_ques_cat(request):
    if request.method == 'POST' and request.is_ajax:
        cat_id = request.POST.get('cat_id')
        cat = models.Category.objects.get(pk=cat_id)
        questions = models.Question.objects.filter(cat_name=cat)
        ques_json = serializers.serialize('json', questions)
        return HttpResponse(ques_json, content_type='application/json')


def result_list(request):
    context = {"results": models.FinalResult.objects.all()}
    return render(request, 'exam/result_list.html', context)
