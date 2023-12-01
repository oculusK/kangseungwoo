from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
from polls.forms import NameForm
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # 화면 보여줄려면 render 써야함

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # DB에 아무것도 안넣었다면 404 낫 파운드
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    logger.debug(f"vote().question_id: {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여 준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리 하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid(): # 폼에 담긴 데이터가 유효한지 체크
            new_name = form.cleaned_data['name']
            return HttpResponseRedirect('')
    else:
        form = NameForm()
    return render(request, 'polls/name.html', {'form': form})