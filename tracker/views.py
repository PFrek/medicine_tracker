from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import TimeSpot, Medicine
from datetime import datetime

# Create your views here.
class TimeSpotListView(generic.ListView):
    model = TimeSpot
    template_name = "timespot_list.html"
    context_object_name = "timespots"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = self.current_time.strftime('%H:%M:%S')
        return context
    
    def get_queryset(self):
        # self.current_time = datetime.now()
        self.current_time = datetime.strptime("06:00:00", "%H:%M:%S")
        queryset = {
            'previous_spot': TimeSpot.objects.filter(time__lte=self.current_time).order_by('-time')[:1],
            'next_spot': TimeSpot.objects.filter(time__gt=self.current_time)[:1],
        }
        if not queryset['next_spot']:
            queryset['next_spot'] = TimeSpot.objects.all().order_by('time')[:1]
         
        if not queryset['previous_spot']:
            queryset['previous_spot'] = TimeSpot.objects.all().order_by('-time')[:1]
            
        return queryset
    
class MedicineDetailView(generic.DetailView):
    model = Medicine