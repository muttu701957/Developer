from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.db.models import Count
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login.html')
            
    return render(request,'login.html')

def regsiter(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        redirect('login')

    
    return render(request,'register.html')

def header(request):
    return render(request,'header.html')

def sidebar(request):
    return render(request,'sidebar.html')

def system_settings(request):
    return render(request,'system_settings.html')

def footer(request):
    return render(request,'footer.html')

def add_pure_item(request):
    return render(request,'add_pure_item.html')

def purchage_add(request):
    form = PurchageForm()
    if request.method == 'POST':
        form = PurchageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/purchage_list')
    context = {'form':form}
    return render(request,'purchage_add.html',context)

def purchage_list(request):
    form = Purchagemaster.objects.all()
    context={'form':form}
    return render(request,'purchage_list.html',context)


def customer_add(request):
    form = customerform()
    if request.method == 'POST':
        form = customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer_list')
    context={'form':form}
    return render(request,'customer_add.html',context)

def customer_list(request):
    form = customer.objects.all()
    context={'form':form}
    return render(request,'customer_list.html',context)

def customer_delete(request,id):
    item = customer.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('customer_list')
    context ={'item':item}
    return render(request,'customer_delete.html',context)

def nursery_add(request):
    form = Nurseryform()
    if request.method == 'POST':
        form = Nurseryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/nursery_list')
    context = {'form':form}
    return render(request,'nursery_add.html',context)

def nursery_add_mul(request):
    return render(request,'nursey_add_mul.html')

def nursery_delete(request,id):
    item = Nurserymaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('/nursery_list')
    context ={'item':item}
    return render(request,'nursery_delete.html',context)


def nursery_list(request):
    form = Nurserymaster.objects.all()
    context={'form':form}
    return render(request,'nursery_list.html',context)


def invoice_nursery(request,pk):
    form = Nurserymaster.objects.get(id=pk)
    context ={'form':form}
    return render(request,'invoice_nursery.html',context)


def nursery_ledger(request):
    form = Nurserymaster.objects.raw("SELECT * FROM nursery_Nurserymaster GROUP BY farmer_name")
    context={'form':form}
    return render(request,'nursery_ledger.html',context)


def ledger_invoice(request,farmer_name):
    form = Nurserymaster.objects.filter(farmer_name=farmer_name)
    context={'form':form}
    return render(request,'ledger_invoice.html',context)

def party_invoice(request,pk):
    form = PartylistMaster.objects.get(id=pk)
    context = {'form':form}
    return render(request,'party_invoice.html',context)


def partyfinal_invoice(request):
    return render(request,'partyfinal_invoice.html')


def partylist_delete(request):
    form = PartylistdeleteMaster.objects.all()
    context={'form':form}
    return render(request,'partydelete.html',context)





def pb_customer_add(request):
    form = PBcustomerform()
    if request.method == 'POST':
        form = PBcustomerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pb_customers')
    context={'form':form}
    return render(request,'pb_customer_add.html',context)


def pbcustomer_delete(request,id):
    item =PBcustomerMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('pb_customers')
    context ={'item':item}
    return render(request,'pb_customer_delete.html',context)

def pb_sugarcane_delete(request,id):
    item =PbsugarcaneMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('pb_sugarcane')
    context ={'item':item}
    return render(request,'pb_sugarcane_delete.html',context)

def pb_sugarcane(request):
    form = PbsugarcaneMaster.objects.all()
    context={'form':form}
    return render(request,'pb_sugarcane.html',context)

def pb_customers(request):
    form = PBcustomerMaster.objects.all()
    context={'form':form}
    return render(request,'pb_customers.html',context)

def pb_ledger(request):
    form = PbsugarcaneMaster.objects.all()
    context={'form':form}
    return render(request,'pb_ledger.html',context)






def pb_sugarcane_add(request):
    form = Pbsugarcaneform()
    if request.method == 'POST':
        form = Pbsugarcaneform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pb_sugarcane')
    context={'form':form}
    return render(request,'pb_sugarcane_add.html',context)



def pb_invoice(request,pk):
    form = PbsugarcaneMaster.objects.get(id=pk)
    context = {'data':form}    
    return render(request,'pb_invoice.html',context)

def add_pure_item(request):
    form = addpureMaster()
    if request.method == 'POST':
        form = addpureform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_pure_item')
    context={'form':form}
    form = addpureMaster.objects.all()
    context={'form':form}
    return render(request,'add_pure_item.html',context)

def add_pure_edit(request,pk):
    task = addpureMaster.objects.get(id=pk)
    form = addpureform(instance=task)
    if request.method == 'POST':
        form = addpureform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/add_pure_item')
    context={'form':form,
             'task':task}
    return render(request,'add_pure_edit.html',context)

def add_pure_delete(request,id):
    item = addpureMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('/add_pure_item')
    context ={'item':item}
    return render(request,'add_pure_delete.html',context)

def purchage_list_delete(request,id):
    item = Purchagemaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('/purchage_list')
    context ={'item':item}
    return render(request,'purchage_list_delete.html',context)

def pb_invoice2(request,pk):
    form = PbsugarcaneMaster.objects.get(id=pk)
    context = {'data':form}
    return render(request,'pb_invoice2.html',context)

def sb_customer(request):
    form = SBcustomerMaster.objects.all()
    context={'form':form}
    return render(request,'sb_customer.html',context)

def sb_customer_add(request):
    form = Sbcustomerform()
    if request.method =='POST':
        form=Sbcustomerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sb_customer')
    context={'form':form}
    return render(request,'sb_customer_add.html',context)

def sb_customer_delete(request,id):
    item = SBcustomerMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('sb_customer')
    context ={'item':item}
    return render(request,'sb_customer_delete.html',context)
    

def sb_sugar(request):
    form = SbsugarMaster.objects.all()
    context ={'form':form}
    return render(request,'sb_sugarcane.html',context)

def sb_sugar_add(request):
    form = sugarcanesbform()
    if request.method == 'POST':
        form=sugarcanesbform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sb_sugar')
    context = {'form':form}
    return render(request,'sb_sugarcane_add.html',context)

def sb_sugarcane_delete(request,id):
    item = SbsugarMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('sb_sugarcane')
    context ={'item':item}
    return render(request,'sb_sugarcane_delete.html',context)

def sb_ledger(request):
    form = SbsugarMaster.objects.all()
    context ={'form':form}
    return render(request,'sb_sugarcane.html',context)

def labour(request):
    form = LabourMaster.objects.all()
    context ={'form':form}
    return render(request,'labour.html',context)

def labour_add(request):
    form = labourform()
    if request.method == 'POST':
        form = labourform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/labour')
    context={'form':form}
    return render(request,'labour_add.html',context)

def labour_customer_delete(request,id):
    item = LabourMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('labour')
    context ={'item':item}
    return render(request,'labour_customer_delete.html',context)

def sugar_invoice(request,pk):
    form = SbsugarMaster.objects.get(id=pk)
    context = {'form':form}
    return render(request,'sugar_invoice.html',context)

def view_labour(request):
    form = sclabourMaster.objects.all()
    context ={'form':form}
    return render(request,'view_labour.html',context)

def view_labour_delete(request,id):
    item = sclabourMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('view_labour')
    context ={'item':item}
    return render(request,'view_labour_delete.html',context)

def sc_labour_add(request):
    form = sclabourform()
    if request.method == 'POST':
        form = sclabourform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_labour')
    context={'form':form}
    return render (request,'sc_labour_add.html',context)

def view_ledger(request):
    form = sclabourMaster.objects.all()
    context ={'form':form}
    return render(request,'view_ledger.html',context)

def in_cust_add(request):
    form = inCustForm()
    if request.method == 'POST':
        form = inCustForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/in_cust')
    context={'form':form}
    return render(request,'in_customer_add.html',context)

def in_cust(request):
    form=incustMaster.objects.all()
    context={'form':form}
    return render(request,'in_customer.html',context)

def in_cust_delete(request,id):
    item = incustMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('in_cust')
    context ={'item':item}
    return render(request,'in_customer_delete.html',context)
    

def in_list_add(request):
    form = inlistform()
    if request.method == 'POST':
        form = inlistform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('in_list')
    context={'form':form}
    return render(request,'in_list_add.html',context)


def in_list(request):
    form = inlistMaster.objects.all()
    context={'form':form}
    return render(request,'in_list.html',context)

def in_list_delete(request,id):
    item = inlistMaster.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('in_list')
    context ={'item':item}
    return render(request,'in_list_delete.html',context)