from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from shealth.models import Doctor, Patient, Appointment
from shealth.forms import DoctorForm, PatientForm


class DoctorRegisterView(APIView):
    def post(self, request):
        print(request.data)
        form = DoctorForm(request.data)
        if form.is_valid():
            obj = form.save(commit=False)
            password = form.cleaned_data.get('password')
            obj.password = make_password(password)
            obj.save()

            return Response({'detail': 'Doctor registered successfully'})
        else:
            return Response({'detail': 'Doctor registration failed', 'errors': form.errors})


class PatientRegisterView(APIView):
    def post(self, request):
        form = PatientForm(request.data)
        if form.is_valid():
            obj = form.save(commit=False)
            password = form.cleaned_data.get('password')
            obj.password = make_password(password)
            obj.save()

            return Response({'detail': 'Patient registered successfully'})
        else:
            return Response({'detail': 'Patient registration failed', 'errors': form.errors})
            

class Index(APIView):
    def get(self, request):
        return Response({'detail': 'Shealth'})