from django.shortcuts import render
from incidentdown.models import IncidentDown
from django.http import HttpResponse
import csv
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'generatereport/index.html')

#Generate CSV
def generate_csv(request):
    # Query all records from YourModel
    queryset = IncidentDown.objects.all()

     # Get the current date
    current_date = datetime.now().strftime('%Y%m%d')

    # Specify the file path
    csv_file_path = 'websnow.csv'

    # Write data to CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header
        header = [field.name for field in IncidentDown._meta.fields]
        csv_writer.writerow(header)

        # Write the data
        for row in queryset:
            csv_writer.writerow([getattr(row, field) for field in header])

    # Send the CSV file as a response
    with open(csv_file_path, 'rb') as csv_response:
        response = HttpResponse(csv_response.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="incidentwhensnowisdowm_{current_date}.csv"'
        return response