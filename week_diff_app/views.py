from django.shortcuts import render, HttpResponse
from django.http import Http404
from datetime import datetime
from .utils import diff_weeks, format_date
 
def index(request):
    
    #today = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    today = datetime.today()#.strftime('%Y-%m-%d')
    zora_dob = datetime(2021, 7, 28)#.strftime('%Y-%m-%d')
    zora_pred_dob = datetime(2021, 8, 2)#.strftime('%Y-%m-%d')
    
    zora_age = diff_weeks(zora_dob, today)
    zora_age_since_pred = diff_weeks(zora_pred_dob, today)
    
    return render(request, 'week_diff_app/index.html', 
                  dict(today = format_date(today), 
                       zora_dob = format_date(zora_dob),
                       zora_pred_dob = format_date(zora_pred_dob), 
                       zora_age = zora_age,
                       zora_age_since_pred = zora_age_since_pred
                       )
                  
                  )

def custom_date(request, id):

    try:
        year = int(id[0:4])
        month = int(id[4:6])
        day = int(id[6:8])
        entered_date = datetime(year, month, day)
        
    except:
        raise Http404("Page does not exist. Wrong date.")
    
    today = datetime.today()
    age = diff_weeks(entered_date, today)
    
    return render(request, 'week_diff_app/custom_date.html', 
                  dict(today = format_date(today), 
                       entered_date = format_date(entered_date),
                       age = age
                       )
                  
                  )