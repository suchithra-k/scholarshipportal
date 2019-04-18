from django import forms

from users.models import StudentProfile, Organisation
from users.user_constants import UserConstant


class SearchForm(forms.Form):
    marks = forms.FloatField(required=False)
    year = forms.ChoiceField(choices=UserConstant.YEAR_CHOICES, required=False)
    caste = forms.ChoiceField(
        choices=UserConstant.CASTE_CHOICES, required=False)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['institution', 'degree', 'course',
                  'academic_year', 'marks', 'caste']

    def save(self, user):
        instance = super(ProfileUpdateForm, self).save(commit=False)
        student_profile = StudentProfile.objects.filter(user=user).first()
        if student_profile is None:
            instance.user = user
            instance.save()
        else:
            student_profile.institution = instance.institution
            student_profile.degree = instance.degree
            student_profile.course = instance.course
            student_profile.academic_year = instance.academic_year
            student_profile.marks = instance.marks
            student_profile.caste = instance.caste
            student_profile.save()


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['name', 'address']

    def save(self, user):
        instance = super(OrganisationForm, self).save(commit=False)
        organisation = Organisation.objects.filter(user=user).first()
        if organisation is None:
            instance.user = user
            instance.save()
        else:
            organisation.name = instance.name
            organisation.address = instance.address
            organisation.save()


class ScholarshipForm(forms.Form):
    YEAR_CHOICES = (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
    )
    CASTE_CHOICES = (
        ('OC', 'OC'),
        ('BC', 'BC'),
        ('MBC', 'MBC'),
        ('BCM', 'BCM'),
        ('SC', 'SC'),
        ('ST', 'ST')
    )
    scholarship_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    title = forms.CharField()
    url = forms.CharField(widget=forms.URLInput)
    expiry_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'), help_text="Date Format: YYYY-MM-DD")
    mininum_marks = forms.FloatField()
    year = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=YEAR_CHOICES)
    caste = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=CASTE_CHOICES)
