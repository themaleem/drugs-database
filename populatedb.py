import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')

import django
import csv
from django.utils.timezone import datetime

# Import settings
django.setup()
csvobj=csv.reader(open('drugs.csv','r'))
from drugs.models import Drug
all_drugs=list(csvobj)[1:]


def populate():
    '''
    Create N Entries of Dates Accessed
    '''
    if all_drugs:
        print(len(all_drugs))
        print('found em')    
        for i in all_drugs:
            approv_to_datetime = datetime.strptime(i[8], '%Y-%m-%d')
            exp_to_datetime=datetime.strptime(i[9],'%Y-%m-%d %H:%M:%S')
            drug = Drug.objects.get_or_create(
                                                name=i[2],
                                                active_ingredient=i[4],
                                                applicant_name =i[5],
                                                country = i[6],
                                                manufacturer = i[7],
                                                date_approv = approv_to_datetime,
                                                exp_date = exp_to_datetime,
                                                reg_no = i[10])[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')
