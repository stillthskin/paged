Steps to Django Setup
1. Create project. //django-admin startproject
2. Create app. //python3 manage.py startapp 
3. Mod project settings.py add installed apps // 'name.apps.NameConfig', 
4. {Always migrate to update python3 manage.py migrate
    Always migrate to update python3 manage.py makemigrations appname}
5. Model your DB. class tablename/modelname(models.Model): ID AutoAdded
6. import Models // from .models import modelname
7. Create object of model. // model = modelname(name=name,etc)
8. object.save()
0. python3 manage.py runserver
. urls include include()
userCreationForm from django.auth.forms
usercreationform object
context ={form = form}
forms 
createuserform(createUserForm):
        model = modename
        fields = [modelfied, modelfield2]
        
createuserform from .forms
