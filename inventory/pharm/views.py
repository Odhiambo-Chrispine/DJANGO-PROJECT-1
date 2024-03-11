from unicodedata import category
from django.shortcuts import redirect, render
from . forms import *
from . models import *

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth

from django.http import HttpResponse
import csv

from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def admin(request):
    return render(request,'admin.html')

def navbar(request):
    return render(request,'navbar.html')

@login_required(login_url='login')
def items(request):
    title = 'List of items in the store'
    form = ItemSearchForm(request.POST or None)
    queryset = Items.objects.all()
    context={'title':title,'form':form,'queryset':queryset}
    if request.method == 'POST':
        queryset=Items.objects.filter(item_name=form['item_name'].value())
        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type = 'text/csv')
            response['Content-Disposition']='attachment: filename="stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['category','item_name','quantity_of_packs'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category,stock.item_name,stock.quantity_of_packs])
            return response
    context={'title':title,'form':form,'queryset':queryset}
    return render(request,'items.html',context)

def others(request):
    title = 'Other Details of the Items'
    queryset = Items.objects.all()
    context={'title':title,'queryset':queryset}
    return render(request,'others.html',context)

def issue(request):
    title = 'Other Details of the Items'
    queryset = Items.objects.all()
    context={'title':title,'queryset':queryset}
    return render(request,'issue.html',context)

def add(request):
    form = ItemCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'you have successfully added an item!')

        return redirect('items')
    context = {'form':form,'title':'Add Items'}
    return render(request,'add.html',context)

def update(request,pk):
    queryset = Items.objects.get(id=pk)
    form = ItemUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ItemUpdateForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request,'you have successfully updated an item!')

            return redirect('items')
    context = {'form':form}
    return render(request,'add.html',context)

def delete(request,pk):
    queryset = Items.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request,'you have successfully deleted an item!')

        return redirect('items')
    return render(request,'delete.html')

def detail(request,pk):
    queryset = Items.objects.get(id=pk)
    context = {'queryset':queryset}
    return render(request,'detail.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
        
    return render(request,'register.html',context={'registerForm':form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)
            if user is not None:
                auth.login(request,user)

                return redirect('items')

    return render(request,'login.html',context={'loginForm':form})

def user_logout(request):
    return render(request,'home.html')

def issue_item(request,pk):
    queryset = Items.objects.get(id=pk)
    form = IssueForm(request.POST or None,instance=queryset)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity_of_packs -= instance.quantity_issued
        #instance.issued_by_internally = str(request.user)
        messages.success(request, 'issued successfully ' + str(instance.quantity_of_packs) + " " + str(instance.item_name)+ ' now left in the store.')
        instance.save()

        return redirect('/detail/'+str(instance.id))
    
    context = {'title':'issued '+str(queryset.item_name),'form':form,'queryset':queryset,'username':'issued by '+str(request.user)}

    return render(request,'add.html',context)

def receive_item(request,pk):
    queryset = Items.objects.get(id=pk)
    form = ReceiveForm(request.POST or None,instance=queryset)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity_of_packs += instance.quantity_received
        #instance.issued_by_internally = str(request.user)
        instance.save()
        messages.success(request, 'received successfully ' + str(instance.quantity_of_packs) + " " + str(instance.item_name)+ ' now in the store.')

        return redirect('/detail/'+str(instance.id))
    
    context = {'title':'received '+str(queryset.item_name),'form':form,'queryset':queryset,'username':'issued by '+str(request.user)}

    return render(request,'add.html',context)

def reorder_level(request,pk):
    queryset = Items.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None,instance=queryset)

    if form.is_valid():
        instance = form.save(commit=False) 
        instance.save()
        messages.success(request, 'reorder level for '+str(instance.item_name)+ " is updated to " + str(instance.reorder_level))

        return redirect('/items')
    
    context = {'form':form,'queryset':queryset}

    return render(request,'add.html',context)