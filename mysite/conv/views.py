from django.shortcuts import render
from .models import ConVModels
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from ...convcrawler.ConVData import nCoV_2019
# from pyecharts import options as opts
# from pyecharts.faker import Faker

# Create your views here.
def indexPage(request):
    return render(request,'templates/indexPage.html')

def selectsf(request):
    return render (request,'templates/selectsf.html')

def selectsfByConditions(request):
    # nCoV_2019 = nCoV_2019()
    # nCoV_2019.main()
    if request.POST:
        mydic={}
        preMydic(mydic,request)
        request.session['mydic']=mydic

        print('session1:', request.session.get('mydic'))
        if mydic:
            datas=ConVModels.objects.filter(**mydic)
        else:
            datas=ConVModels.objects.all()
    if request.GET:
        mydic=request.session.get('mydic')
        if mydic:
            datas=ConVModels.objects.filter(**mydic).order_by('mid')
        else:
            datas=ConVModels.objects.all().order_by('mid')
    paginator = Paginator(datas, 10)  # 分页器 Show 25 contacts per page

    page = request.GET.get('page')
    print('page', page)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    x_data,y_data=preconvdata(datas)#横纵坐标





    return render(request,'templates/selectsf.html',context={'contacts':contacts,'x_data':x_data,'y_data':y_data}
                  )


def preMydic(mydic,request):
    name=request.POST['name']
    if name!='0':
        mydic['name']=name

    return mydic
def preconvdata(datas):
    nowConfirm_datas_ls=[]
    confirm_datas_ls = []
    suspect_datas_ls = []
    dead_datas_ls = []
    heal_datas_ls=[]


    for item in datas:
        nowConfirm_datas_ls.append(item.nowConfirm)
        confirm_datas_ls.append(item.confirm)
        suspect_datas_ls.append(item.suspect)
        dead_datas_ls.append(item.dead)
        heal_datas_ls.append(item.heal)
    nowConfirm_datas=sum(nowConfirm_datas_ls)
    confirm_datas=sum(confirm_datas_ls)
    suspect_datas=sum(suspect_datas_ls)
    dead_datas=sum(dead_datas_ls)
    heal_datas=sum(heal_datas_ls)


    x_data=['现存确诊','疑似病例','死亡人数']
    y_data=[nowConfirm_datas,suspect_datas,dead_datas]
    print(y_data)
    return x_data,y_data



    # return render
    # (requests,'selectsf.html',context=)
