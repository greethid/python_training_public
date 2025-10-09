from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """Home page for the learning log app"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Display all topics"""
    topics = Topic.objects.order_by('date_added')
    # Allow to display on the blog topics related to current user only:
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Display a single topic and all related posts"""
    topic = Topic.objects.get(id=topic_id)
    # Make sure that the topic belongs to the current user
    # if topic.owner != request.user:
    #     raise Http404
    # check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # no data was submitted, create a new form
        form = TopicForm()
    else:
        # data was passed via a POST request, it needs to be processed
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display the empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a specific topic"""
    topic = Topic.objects.get(id=topic_id)

    # Make sure that the entry belongs to the current user
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # no data was submitted, create a new form
        form = EntryForm()
    else:
        # data was passed via a POST request, it needs to be processed
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display the empty form
    context = {'topic': topic,'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure that the entry belongs to the current user
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # initial request, filling out the form with the current content of the entry
        form = EntryForm(instance=entry)
    else:
        # data was passed via a POST request, it needs to be processed
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    # Display the empty form
    context = {'entry': entry, 'topic': topic,'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request, topic):
    """Make sure that the topic belongs to the current user"""
    if topic.owner != request.user:
        raise Http404


