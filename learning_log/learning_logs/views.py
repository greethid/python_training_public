from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """Home page for the learning log app"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Display all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Display a single topic and all related posts"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # no data was submitted, create a new form
        form = TopicForm()
    else:
        # data was passed via a POST request, it needs to be processed
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display the empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
