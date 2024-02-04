from django.shortcuts import render, redirect
from django.contrib import messages
from incidentdown.models import IncidentDown, SnowIncident
from django.http import HttpResponse
import csv


# Create your views here.
def index(request):
    return render(request, 'incidentdown/index.html')

def incidentToPush(request):
    if request.method == 'POST':
        caller_id = request.POST['caller_id']
        email = request.POST['email']
        description = request.POST['description']
        comments = request.POST['comments']
        impact = request.POST['impact']
        urgency = request.POST['urgency']
        worknotes = request.POST['worknotes']
        assignment_group = request.POST['assignment_group']
        state = request.POST['state']

    myincident = SnowIncident(
        name = caller_id,
        email = email, 
        description = description,
        comments = comments,
        impact = impact,
        urgency = urgency,
        worknotes = worknotes,  
        assignment_group = assignment_group,
        state = state

    )

    myincident.save()
    messages.success(request, 'Your incident has been submitted')
    return redirect('index')



