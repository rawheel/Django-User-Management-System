from django.shortcuts import render,redirect
from .forms import UserForm,RoleForm,RightsForm
from .models import UserTable,UserRole,UserRights
def show_users(request):
    if request.method == "GET":
        users = list(UserTable.objects.values_list('user_name', flat=True).order_by('id'))
        users_list = {'users_list':users}
        return render(request, "UMS/show_users.html",users_list)
    else:
        value = request.POST['drop1']

        users = UserTable.objects.get(user_name = value)
        roles = UserRole.objects.get(id=users.role_id)
        role_name = roles.role_name

        try:
            rights = UserRights.objects.filter(role=users.role)
            for i in rights:
                print(i.rights_name)

            print("check 1")
            rights_name = i.rights_name
            print("check 2")
            rights_details = i.rights_details
        except Exception as e:
            print(e)

            rights_name = 'No Rights Assigned!'
            rights_details = '-'

        full_name = f'{users.first_name} {users.last_name}'

        #print(full_name,roles.role_name,rights.rights_name,rights.rights_details)

        return render(request,"UMS/showdata.html",{'full_name':full_name,'role_name':role_name,'rights_name':rights_name,'rights_details':rights_details,'rights':rights})

def users_form(request):
    if request.method == "GET":
        form = UserForm()
        return render(request,"UMS/users_form.html",{'form':form})
    else:
        form = UserForm(request.POST)

        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
        else:
            print(form.errors)
            print("invalid")



        return redirect('/users')
def roles_form(request):
    if request.method == "GET":
        form = RoleForm()
        return render(request,"UMS/roles_form.html",{'form':form})
    else:
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/roles')

def rights_form(request):
    if request.method=="GET":
        form = RightsForm()
        return render(request,"UMS/rights_form.html",{'form':form})
    else:
        form = RightsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/rights')