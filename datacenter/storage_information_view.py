from datacenter.models import Passcard, Visit
from django.shortcuts import render


def storage_information_view(request):
    visits_inside = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits_inside:
        duration = visit.format_duration()
        serialized_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': visit.is_visit_long(),
        }
        non_closed_visits.append(serialized_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
