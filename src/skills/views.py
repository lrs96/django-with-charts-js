from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Skill
from profiles.models import Profile

# Create your views here.

def skill_view(request):
    user_id = request.user.id
    profile = Profile.objects.get(pk=user_id)
    SkillFormset = inlineformset_factory(
        Profile, Skill, fields='__all__', extra=1, can_delete=True)

    formset = SkillFormset( request.POST or None,instance=profile)
    if formset.is_valid():
        formset.save()
        redirect('skills/add.html')

    return render(request, 'skills/add.html', {'formset': formset})