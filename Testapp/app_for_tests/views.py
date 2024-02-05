from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Question, Answer, Result


def index(request):
    test_list = Test.objects.all()
    template = 'app_for_tests/index.html'
    context = {'test_list': test_list,}
    return render(request, template, context)


def choose_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    question_list = Question.objects.filter(test=test)
    template = 'app_for_tests/choose_test.html'
    context = {'test': test, 'question_list': question_list}
    return render(request, template, context)


def choose_question(request, test_id, question_id):
    test = get_object_or_404(Test, pk=test_id)
    question = get_object_or_404(Question, pk=question_id)
    answer_list = Answer.objects.filter(question=question)
    template = 'app_for_tests/choose_question.html'
    context = {'test': test, 'question': question, 'answer_list': answer_list}
    return render(request, template, context)


def test_result(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    question_list = Question.objects.filter(test=test)
    template = 'app_for_tests/test_result.html'
    context = {'test': test, 'question_list': question_list}
    return render(request, template, context)


def test_create(request):
    template = 'app_for_tests/test_create.html'
    return render(request, template)
