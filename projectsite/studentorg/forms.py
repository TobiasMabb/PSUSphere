from django.forms import ModelForm
from django import forms
from .models import OrgMember, Organization, Student

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"