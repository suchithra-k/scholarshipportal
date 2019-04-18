from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from crawler.models import Scholarship, ScholarshipEligibility
from users.models import Organisation, StudentProfile

from .forms import (OrganisationForm, ProfileUpdateForm, ScholarshipForm,
                    SearchForm)
from .models import OrganisationScholarship


class ListScholarships(LoginRequiredMixin, View):

    def get_scholarship(self, request, filter=None):
        marks = year = caste = None
        if filter is not None:
            marks = filter['marks']
            year = filter['year']
            caste = filter['caste']

        scholarship_list = Scholarship.objects.filter_with_eligibility(
            marks=marks, year=year, caste=caste)

        return scholarship_list

    def get(self, request, *args, **kwargs):
        clear = request.GET.get('clear')
        form = SearchForm()
        filter = None

        student_profile = StudentProfile.objects.filter(
            user=request.user).first()

        if student_profile is not None and clear is None:
            filter = {
                'marks': student_profile.marks,
                'year': student_profile.academic_year,
                'caste': student_profile.caste
            }

            form = SearchForm(initial=filter)

        if student_profile is None:
            messages.warning(request,
                             'Your profile is not yet updated. Please update your details <a href="%s" target="blank">here</a>' % reverse('profile_update'))

        context = {
            'schloarships': self.get_scholarship(request, filter=filter),
            'form': form
        }
        return render(request, "portal/list_scholarship.html", context)

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        filter = None
        if form.is_valid():
            marks = form.cleaned_data['marks']
            year = form.cleaned_data['year']
            caste = form.cleaned_data['caste']

            filter = {
                'marks': marks,
                'year': year,
                'caste': caste
            }

        context = {
            'schloarships': self.get_scholarship(request, filter=filter),
            'form': form
        }
        return render(request, "portal/list_scholarship.html", context)


class UpdateProfile(LoginRequiredMixin, View):

    def get(self, request):
        form = ProfileUpdateForm()
        student_profile = StudentProfile.objects.filter(
            user=request.user).first()

        if student_profile is not None:
            form = ProfileUpdateForm(instance=student_profile)
        return render(request, "portal/update_profile.html", {'form': form})

    def post(self, request):
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(
                request, 'Your profile has been updated sucessfully')
        return render(request, "portal/update_profile.html", {'form': form})


class ShowOrganistionSchloarship(LoginRequiredMixin, View):

    def get(self, request):
        org_realtion = OrganisationScholarship.objects.filter(
            organisation__user=request.user).select_related('scholarship')
        context = {
            'scholarships': org_realtion
        }
        return render(request, "portal/organisation_home.html", context=context)


class EditOrganisation(LoginRequiredMixin, View):

    def get(self, request):
        form = OrganisationForm()
        organisation = Organisation.objects.filter(
            user=request.user).first()

        if organisation is not None:
            form = OrganisationForm(instance=organisation)
        return render(request, 'portal/edit_organisation.html', context={'form': form})

    def post(self, request):
        form = OrganisationForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(
                request, 'Your details has been updated sucessfully')
        return render(request, "portal/edit_organisation.html", {'form': form})


class NewScholarship(LoginRequiredMixin, View):

    def get(self, request):
        form = ScholarshipForm()
        scholarship_id = request.GET.get('id')
        if scholarship_id is not None:
            scholarship = Scholarship.objects.get(pk=scholarship_id)
            s_eligibility = scholarship.scholarshipeligibility
            initial = {
                'scholarship_id': scholarship_id,
                'title': scholarship.title,
                'url': scholarship.url,
                'expiry_date': scholarship.expiry_date,
                'mininum_marks': s_eligibility.min_marks,
                'year': s_eligibility.year,
                'caste': s_eligibility.caste
            }
            form = ScholarshipForm(initial=initial)

        return render(request, 'portal/scholarship_entry.html', context={'form': form})

    def post(self, request):
        form = ScholarshipForm(request.POST)
        if form.is_valid():
            scholarship_id = form.cleaned_data['scholarship_id']
            title = form.cleaned_data['title']
            url = form.cleaned_data['url']
            expiry_date = form.cleaned_data['expiry_date']
            years = form.cleaned_data['year']
            mininum_marks = form.cleaned_data['mininum_marks']
            caste = form.cleaned_data['caste']

            if scholarship_id != "":
                sch = Scholarship.objects.get(pk=scholarship_id)
                sch.title = title
                sch.url = url
                sch.expiry_date = expiry_date
                sch.save()
                sch.refresh_from_db()
                sch.scholarshipeligibility.min_marks = mininum_marks
                sch.scholarshipeligibility.year = years
                sch.scholarshipeligibility.caste = caste
                sch.scholarshipeligibility.save()
                messages.success(
                    request, 'Scholarship updated sucessfully')
            else:
                new_scholarship = Scholarship(
                    title=title, url=url, expiry_date=expiry_date)
                new_scholarship.save()

                ScholarshipEligibility(
                    scholarship=new_scholarship, min_marks=mininum_marks, year=years, caste=caste).save()

                OrganisationScholarship(
                    organisation=request.user.organisation, scholarship=new_scholarship).save()
                messages.success(
                    request, 'Scholarship added sucessfully')
            return redirect('organisation_home')
        return render(request, 'portal/scholarship_entry.html', context={'form': form})


class DeleteScholarship(LoginRequiredMixin, View):

    def get(self, request, sid):
        Scholarship.objects.get(pk=sid).delete()
        messages.success(
            request, 'Scholarship Deleted Successfully')
        return redirect('organisation_home')
