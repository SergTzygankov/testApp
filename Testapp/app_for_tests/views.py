from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Test, Question, Answer, Result
from .forms import TestForm, QuestionForm, AnswerForm


def index(request):
    test_list = Test.objects.all()
    template = 'app_for_tests/index.html'
    context = {'test_list': test_list,}

    return render(request, template, context)


def test_create(request):
    template = 'app_for_tests/test_create.html'
    context = {'test_form': test_form,}
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        if test_form.is_valid():
            test = test_form.save()
            for key, value in request.POST.items():
                if key.startswith('question_text_'):
                    question_text = value
                    question = QuestionForm({'text': question_text})
                    if question.is_valid():
                        question = question.save(commit=False)
                        question.test = test
                        question.save()
                        question_index = key.split('_')[-1]
                        for i in range(4):
                            answer_text = request.POST.get(f'answer_text_{question_index}_{i}', '')
                            is_correct = request.POST.get(f'is_correct_{question_index}_{i}', False)
                            answer = AnswerForm({'text': answer_text, 'is_correct': is_correct})
                            if answer.is_valid():
                                answer = answer.save(commit=False)
                                answer.question = question
                                answer.save()
            return redirect('/')
    else:
        test_form = TestForm()
    return render(request, template, context)


def choose_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    question_list = Question.objects.filter(test=test)
    template = 'app_for_tests/choose_test.html'
    context = {'test': test,
               'question_list': question_list,}
    return render(request, template, context)


def start_test(request, test_id):
    test = Test.objects.get(pk=test_id)
    questions = Question.objects.filter(test=test)
    template = 'app_for_tests/start_test.html'
    context = {'test': test, 'questions': questions}

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        if user_name:
            # Получение ответов пользователя на вопросы
            user_answers = {}
            for question in questions:
                answer_id = request.POST.get(f'answer_{question.id}')
                if answer_id:
                    user_answers[question] = int(answer_id)

            # Вычисление результата теста
            score = 0
            for question, chosen_answer_id in user_answers.items():
                correct_answer_id = question.answer_set.filter(is_correct=True).first().id
                if chosen_answer_id == correct_answer_id:
                    score += 1
            result_percentage = round((score / len(questions)) * 100, 2)

            # Создание объекта результата и сохранение его в базе данных
            Result.objects.create(test=test, user=user_name, result=result_percentage)

            # Перенаправление пользователя на страницу с результатом теста
            return HttpResponseRedirect(
                reverse('app_for_tests:test_result', args=[test_id]) + f'?result={result_percentage}&user_name={user_name}')

    return render(request, template, context)


def choose_question(request, test_id, question_id):
    test = get_object_or_404(Test, pk=test_id)
    question = get_object_or_404(Question, pk=question_id)
    answer_list = Answer.objects.filter(question=question)
    template = 'app_for_tests/choose_question.html'
    context = {'test': test,
               'question': question,
               'answer_list': answer_list,}
    return render(request, template, context)


def test_result(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    question_list = Question.objects.filter(test=test)
    result = request.GET.get('result')  # Извлекаем результат из параметра запроса
    user_name = request.GET.get('user_name')

    template = 'app_for_tests/test_result.html'
    context = {'test': test,
               'question_list': question_list,
               'result': result,
               'user_name': user_name,}

    return render(request, template, context)