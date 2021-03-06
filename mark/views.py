from django.shortcuts import render,redirect
from .models import Txt,Marktxt
from account.models import User,Headman
from django.http import HttpResponse
import json

# Create your views here.
def admin(request):
    context={}
    txts=Txt.objects.all()
    users=User.objects.all()
    heads = Headman.objects.all()
    context['txts']=txts
    context['users']=users
    context['heads']=heads
    users=[]
    mark=[]
    array=[]
    p=[]
    n=[]
    yizhi=[]
    index=0
    for txt in txts:
        if Marktxt.objects.filter(txt=txt.title,is_finished=1):
            yizhi.append(1)   
        else:
            yizhi.append(0)
        continue
    for txt in txts:
        a=0
        x=0
        mark.append(Marktxt.objects.filter(txt=txt.title))#每一文章的标记取出来 p=len(mark)
        p.append(len(mark[index]))
        types=[]
        users=[]
        for j in mark[index]:
            if j.is_finished==1:
                yizhi.append(1)
            if j.user not in users:
                users.append(j.user)
            if j.marktxt_type not in types:
                types.append(j.marktxt_type)
        n.append(len(users))
        for i in types:
            type_mark=Marktxt.objects.filter(marktxt_type=i,txt=txt.title)
            start=[]
            end=[]
            for m in type_mark:
                start.append(m.start)
                end.append(m.end)
            if len(set(start))==1 and len(set(end))==1:
                a+=1
        try:
            x=n[index]*a/p[index]
        except:
            pass
        array.append(x)
        index+=1
    context["a"]=array
    context["n"]=n  #人数
    context["p"]=p  
    context["yizhi"]=yizhi
    return render(request,'admin.html',context)

def txt_detail(request,txt_id):
    txt=Txt.objects.get(id=txt_id)
    context={}
    context['txt_obj']=txt
    return render(request,'txt.html',context)

def txt_edit(request,txt_id):
    context2={}
    txt=Txt.objects.get(id=txt_id)
    marktxts=Marktxt.objects.filter(user=request.session['user_name'],txt=txt.title)
    context2['txt_obj']=txt
    context2['marktxts']=marktxts
    types=[]
    context=[]
    start=[]
    end=[]
    for i in marktxts:
        types.append(i.marktxt_type)
        context.append(i.text)
        start.append(i.start)
        end.append(i.end)
    context2['types']=json.dumps(types)
    context2['context']=json.dumps(context)
    context2['start']=json.dumps(start)
    context2['end']=json.dumps(end)
    return render(request,'edit.html',context2)

def finish(request,is_finished,txt_id):
    context2={}
    if is_finished:
        txt=Txt.objects.get(id=txt_id)
        marktxts=Marktxt.objects.filter(is_finished=is_finished,txt=txt.title)
        context2['txt_obj']=txt
        context2['marktxts']=marktxts
        types=[]
        context=[]
        start=[]
        end=[]
        for i in marktxts:
            types.append(i.marktxt_type)
            context.append(i.text)
            start.append(i.start)
            end.append(i.end)
        context2['types']=json.dumps(types)
        context2['context']=json.dumps(context)
        context2['start']=json.dumps(start)
        context2['end']=json.dumps(end)
        return render(request,'edit.html',context2)
    else:
        return render(request,'last.html',context2)

def group_edit(request):
    context2={}
    txt=Txt.objects.get(title=request.session['txt'])
    context2['txt_obj']=txt
    marktxts=[]
    all_type=[]
    all_context=[]
    all_start=[]
    all_end=[]
    if request.method=="POST":
        check_box_list = request.POST.getlist('check_box_list')
        for i in check_box_list:
            marktxts.append(Marktxt.objects.filter(user=i,txt=request.session['txt']))
    for mark in marktxts:
        types=[]
        context=[]
        start=[]
        end=[]
        for i in mark:
            types.append(i.marktxt_type)
            context.append(i.text)
            start.append(i.start)
            end.append(i.end)
        all_type.append(types)
        all_context.append(context)    
        all_start.append(start)    
        all_end.append(end)        
    context2['types']=json.dumps(all_type)
    context2['context']=json.dumps(all_context)
    context2['start']=json.dumps(all_start)
    context2['end']=json.dumps(all_end)
    context2['my_user']=json.dumps(check_box_list)
    return render(request,'groupedit.html',context2)

def txt_list(request):
    if request.session.get('is_login', None):
        context={}
        txts=Txt.objects.filter(group=request.session['group'])
        context['txts']=txts
        my=[]
        my_txts=[]
        marktxts=Marktxt.objects.filter(user=request.session['user_name'])
        for i in marktxts:
            if i.txt not in my:
                my.append(i.txt)
            else:
                pass
        for i in my:
            txt=Txt.objects.get(title=i)
            my_txts.append(txt)
        context['my_txts']=my_txts
        return render(request,'list.html',context)
    return render(request,'list.html')

def txt_refer(request):
    json_receive = json.loads(request.body)
    same_mark=Marktxt.objects.filter(user=json_receive['user'],user_group=json_receive['user_group'],txt=json_receive['txt'])
    if same_mark:
        Marktxt.objects.filter(user=json_receive['user'],marktxt_type=json_receive['marktxt_type'],txt=json_receive['txt']).delete()
    mark=Marktxt()
    mark.marktxt_type=json_receive['marktxt_type']
    mark.start=json_receive['start']
    mark.end=json_receive['end']
    mark.text=json_receive['text']
    mark.user=json_receive['user']
    mark.user_group=json_receive['user_group']
    mark.txt=json_receive['txt']
    mark.is_finished=json_receive['zuizhong']
    mark.save()
    return HttpResponse("success")

def txt_delete(request):
    json_receive = json.loads(request.body)
    Marktxt.objects.filter(user=json_receive['user'],txt=json_receive['txt']).delete()
    return HttpResponse("success")

def txt_download(request):
    json_receive = json.loads(request.body)
    name=request.session['user_name']
    full_path="D:\\desktop\\"+name+'.xml' 
    file=open(full_path,'w')
    file.write(json_receive['content'])
    file.close
    return HttpResponse("success")

def txt_upload(request):
    txt=Txt()
    txt.group=request.POST['group']
    txt.title=request.POST['title']
    txt.content=request.POST['content']
    txt.save()
    return redirect("http://localhost:8000/mark/chargeman")

def charge(request,k):
    context={}
    users=[]
    mark=[]
    array=[]
    p=[]
    n=[]
    yizhi=[]
    index=0
    if request.session.get('is_login',None):
        if request.session.get('is_group', None):
            group_txts = Txt.objects.filter(group=request.session['group'])
            context['group_txts']=group_txts
            for txt in group_txts:
                if Marktxt.objects.filter(txt=txt.title,is_finished=1):
                    yizhi.append(1)   
                else:
                    yizhi.append(0)
                continue
            for txt in group_txts:
                a=0
                x=0
                mark.append(Marktxt.objects.filter(txt=txt.title))#每一文章的标记取出来 p=len(mark)
                p.append(len(mark[index]))
                types=[]
                users=[]
                for j in mark[index]:
                    if j.is_finished==1:
                        yizhi.append(1)
                    if j.user not in users:
                        users.append(j.user)
                    if j.marktxt_type not in types:
                        types.append(j.marktxt_type)
                n.append(len(users))
                for i in types:
                    type_mark=Marktxt.objects.filter(marktxt_type=i,txt=txt.title)
                    start=[]
                    end=[]
                    for m in type_mark:
                        start.append(m.start)
                        end.append(m.end)
                    if len(set(start))==1 and len(set(end))==1:
                        a+=1
                try:
                    x=n[index]*a/p[index]
                except:
                    pass
                array.append(x)
                index+=1
            context["a"]=array
            context["n"]=n  #人数
            context["p"]=p  
            context["k"]=k
            context["yizhi"]=yizhi
            return render(request,'chargeman.html',context)
        else:
            return render(request,'chargeman.html',context)
    else:
        return render(request,'chargeman.html',context)


def mark_detail(request,txt_id):
    context={}
    txt=Txt.objects.get(id=txt_id)
    request.session['txt']=txt.title
    context['txt_obj']=txt
    mark=Marktxt.objects.filter(txt=txt.title)
    context['mark']=mark
    users=[]
    for j in mark:
        if j.user not in users:
            users.append(j.user)
            context['users']=users
    return render(request,'detail.html',context)