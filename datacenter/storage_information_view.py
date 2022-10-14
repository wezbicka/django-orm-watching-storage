from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(time):
    parts_time = str(time).split('.')
    duration = parts_time[0].split(':')
    hours = duration[0]
    minutes = duration[1]
    return f'{hours}ч {minutes}мин'


def storage_information_view(request):
    visits_inside = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visitor in visits_inside:
        duration = format_duration(visitor.get_duration())
        visit = {
            'who_entered': visitor.passcard.owner_name,
            'entered_at': visitor.entered_at,
            'duration': duration,
        }
        non_closed_visits.append(visit)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
