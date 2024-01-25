from django.shortcuts import render
from incidentdown.models import IncidentDown
from django.http import HttpResponse
import csv


# Create your views here.
def index(request):
    return render(request, 'incidentdown/index.html')

def submitincident(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']
        urgency = request.POST['urgency']
        worknotes = request.POST['worknotes']
        assignment_group = request.POST['assignment_group']
        state = request.POST['state']

    myincident = IncidentDown(
        name = name,
        email = email, 
        description = description,
        urgency = urgency,
        worknotes = worknotes,  
        assignment_group = assignment_group,
        state = state

    )

    myincident.save()
    return render(request, 'incidentdown/index.html')

