from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from core.models import description
from django.http import JsonResponse
import json
from django.http import QueryDict   

class index(generic.ListView):
    
    model = description
    template_name = "core/index.html"
    context_object_name = "descriptions"
#     description.objects.create(name='John Doe', address='123 Elm Street, Springfield', email='john.doe@example.com', age=25)
# description.objects.create(name='Jane Smith', address='456 Oak Avenue, Shelbyville', email='jane.smith@example.com', age=30)
# description.objects.create(name='Robert Brown', address='789 Maple Drive, Capital City', email='robert.brown@example.com', age=35)
# description.objects.create(name='Emily Johnson', address='101 Pine Road, Ogdenville', email='emily.johnson@example.com', age=28)
# description.objects.create(name='Michael Lee', address='202 Birch Boulevard, North Haverbrook', email='michael.lee@example.com', age=40)
# description.objects.create(name='Linda Taylor', address='303 Cedar Court, Brockway', email='linda.taylor@example.com', age=22)
# description.objects.create(name='William Harris', address='404 Spruce Lane, Burns', email='william.harris@example.com', age=50)
# description.objects.create(name='Mary Clark', address='505 Willow Way, Springfield', email='mary.clark@example.com', age=29)
# description.objects.create(name='David Martinez', address='606 Chestnut Circle, Shelbyville', email='david.martinez@example.com', age=45)
# description.objects.create(name='Susan Robinson', address='707 Redwood Drive, Capital City', email='susan.robinson@example.com', age=33)

class create(generic.CreateView):
    model = description
    fields = ['name', 'address', 'email', 'age']
    template_name = "core/create.html"
    
def metry(request):
    message = ""
    if request.POST['name'] == "":
        return HttpResponse(message)
    
    message = "This username already exist"
    return HttpResponse(message)

def delete(request, pk):
    
    try:
        description_data = description.objects.get(pk=pk)
        description_data.delete()
        return render(request, 'core/partials/mytext.html', {'descriptions' : description.objects.all()})
    except description.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

def puts(request, pk):
    try:
        if request.method == 'PUT':
            query = QueryDict(request.body)
            description_data = description.objects.get(pk=pk)
            
            description_data.name = query['name']
            description_data.address = query['address']
            description_data.email = query['email']
            description_data.age = query['age']
            
            description_data.save()
            return render(request, 'core/partials/mytext.html', {'descriptions' : description.objects.all()})
         
    except:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)
    
def filter_search(request):
    try:
        search = request.POST['search']
        description_data = description.objects.filter(name__icontains=search)
        return render(request, 'core/partials/mytext.html', {'descriptions' : description_data})
        return HttpResponse("Asd")
    except:
        pass
    
    