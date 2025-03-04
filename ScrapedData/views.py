
from django.shortcuts import render
from .models import MeteoDatas


def table(request):
    meteodatas = MeteoDatas.objects.all()
    return render(request, 'table.html', {'meteodatas': meteodatas})
