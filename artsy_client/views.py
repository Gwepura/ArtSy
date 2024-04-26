from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from dashboard.models import TeamMember

# Create your views here.
def index(request):
    team = TeamMember.objects.filter(active=True).order_by('position')

    return render(request, 'artsy_client/index.html', {
        'team': team,
    })

def view_member_profile(request, id):
    member = TeamMember.objects.get(id=id)

    return HttpResponseRedirect(reverse('index'))