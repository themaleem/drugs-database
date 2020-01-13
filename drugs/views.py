from django.shortcuts import render
from .models import Drug
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse


# API IMPORTS STARTS HERE
from rest_framework import status,generics,viewsets
from rest_framework.response import Response
from .serializers import DrugSerializer
# API IMPORTS ENDS HERE 


# API VIEWS STARTS HERE
class DrugsList(generics.ListCreateAPIView):
    # def get_queryset(self):
    queryset=Drug.objects.all()[:20]     
        # return queryset
    serializer_class=DrugSerializer

# class DrugsViewSet(viewsets.ModelViewSet):
#     queryset=Drug.objects.all()[:20]
#     serializer_class=DrugSerializer



def drug_list(request):
    #First i call all drugs to be listed, search keyword to blank 
    drugs=Drug.objects.all()
    search_keyword=''
    #drug_by_no will remain None if search
    # keyword doesn't match any drug NAFDAC number 
    drug_by_no=None

    if 'title' in request.GET:
        drugs=drugs.order_by('name')

    if 'latest' in request.GET:
        drugs=drugs.order_by('-date_approv')
    
    if 'search' in request.GET:
        search_keyword=request.GET['search'].strip() #Gets the search keyword
        try:
            #checks if keyword matches any drugs NAFDAC number
            # and drugs_by_no returns a Drug object,  then the
            # list is then set to None
            drug_by_no=drugs.get(reg_no=search_keyword)
            drugs=None

            # if the search keyword doesn't matches any drugs NAFDAC number
            # then the drugs list stays and is filtered by keyword
        except Drug.DoesNotExist:
            drugs=drugs.filter(name__icontains=search_keyword)
    
    get_dict_copy=request.GET.copy()
    params=get_dict_copy.pop('page',True) and get_dict_copy.urlencode()

    # if the drugs list or any of its filter exist
    # then run pagination 
    if drugs:
        paginator=Paginator(drugs,50) #paginator object of 50 items per page
        page=request.GET.get('page')
        drugs=paginator.get_page(page)
    
    context={
        'drugs':drugs,
        'params':params,
        'search':search_keyword
    }
    
    # if drug_by_no exists, add it to context dict
    if drug_by_no:
        context['drug_by_no']=drug_by_no
    return render(request,'drugs/all_drugs.html',context)


def drug_detail(request,drug_slug):
    drug=Drug.objects.filter(slug=drug_slug)[0]
    context={
        'drug':drug
    }
    return render(request,'drugs/details.html',context)

def home(request):
    return render(request,'drugs/index.html')