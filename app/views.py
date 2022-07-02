from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import LectureForm, AddQuestionForm
from .models import Lecture, Quiz


# Create your views here.
def index(request):
    topics = Lecture.objects.all()
    context = {'lectures': topics}
    search_lecture = request.GET.get('search')
    if search_lecture:
        lectures = Lecture.objects.filter(Q(name__contains=search_lecture))
    else:
        lectures = Lecture.objects.all()
    return render(request, 'lectures.html', context)


def home(request):
    return render(request, 'index.html')


def tutorial(request):
    tut = Lecture.objects.all()
    user = User.objects.filter(username=request.user.username).all()
    context = {'tut': tut, 'user': user}
    return render(request, 'lectures.html', context)


def quizzes(request):
    obj = Quiz.objects.all()
    context = {'quizzes': obj}
    return render(request, 'quizzes.html', context)


def addLecture(request):
    queryset = Lecture.objects.all()
    if request.method == "POST":
        form_data = LectureForm(data=request.POST)
        if form_data.is_valid():
            lecture = form_data.save(commit=False)
            lecture.name = request.name
            lecture.video = request.video
            lecture.save()
    context = {"form": LectureForm, "lectures": queryset}
    return render(request, "lectures.html", context=context)


def profile(request):
    user = User.objects.filter(username=request.user.username).all()
    context = {"user": user}
    return render(request, "profile.html", context=context)


def addQuestion(request):
    if request.user.is_staff:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'addQuestion.html', context)
    else:
        return redirect('home')


def questions(request):
    if request.method == 'POST':
        print(request.POST)
        ques = Quiz.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in ques:
            total += 1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'result.html', context)
    else:
        ques = Quiz.objects.all()
        context = {
            'questions': ques
        }
        return render(request, 'quiz.html', context)

