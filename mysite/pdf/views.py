from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import studentdetails 
from django.views.generic import View
from pdf import models
import pdfkit


def pdf_download(request, intern_id):
    student=studentdetails.objects.get(id=intern_id)
    
    pdf = pdfkit.from_url(f'http://127.0.0.1:8000/{intern_id}', False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Internship_letter_{student.Name}.pdf"'

    return response
def template(request, intern_id ):
    resultsdisplay=studentdetails.objects.filter(id=intern_id)

    return render(request,'pdf.html',{'studentdetails':resultsdisplay})

