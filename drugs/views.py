from django.shortcuts import render
from .models import Drug
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
# Create your views here.


def drug_list(request):
    drugs=Drug.objects.all()
    search_keyword=''

    if 'title' in request.GET:
        drugs=drugs.order_by('name')

    if 'latest' in request.GET:
        drugs=drugs.order_by('-date_approv')
    
    if 'search' in request.GET:
        search_keyword=request.GET['search']
        try:
            drugs=Drug.objects.filter(reg_no=search_keyword)
        except Drug.DoesNotExist:
            drugs=drugs.filter(name__icontains=search_keyword)
    
    get_dict_copy=request.GET.copy()
    params=get_dict_copy.pop('page',True) and get_dict_copy.urlencode()
    
    paginator=Paginator(drugs,50) #paginator object of 50 items per page
    page=request.GET.get('page') 
    drugs=paginator.get_page(page)
    
    context={
        'drugs':drugs,
        'params':params,
        'search':search_keyword
    }
    return render(request,'drugs/all_drugs.html',context)

# def search(request):
    # text = request.GET.get('nafdacNo')
    # matches = Drug.objects.filter(reg_no=text)
    # searchdict = {
    #     'matches': matches,
    # }
    # return render(request, 'drugs/search.html',)

# def search(request):        
#     if request.method == 'GET': # this will be GET now      
#         text =  request.GET.get('nafdacNO') # do some research what it does       
#         try:
#             matches = drugsdb.objects.filter(name__icontains=text) # filter returns a list so you might consider skip except part
#             return render(request,"drugs/search.html",{"matches":matches})
#     else:
#         return render(request,"drugs/search.html",{})

def drug_detail(request,drug_slug):
    drug=Drug.objects.filter(slug=drug_slug)[0]
    context={
        'drug':drug
    }
    return render(request,'drugs/details.html',context)