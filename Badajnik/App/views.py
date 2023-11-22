from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import default_storage
from django.conf import settings
from .models import Laboratory
import json
from rest_framework import generics
from .models import Laboratory
from .serializers import LaboratorySerializer


def process_address(address):
    if not address:  
        return '', '', '' 

    # Rozdzielanie adresu na części
    parts = address.split(', ')
    if len(parts) < 4:  
        return '', '', '' 

    street_address = parts[1]
    postal_city_parts = parts[2].split(' ')
    postal_code = postal_city_parts[0]
    city = ' '.join(postal_city_parts[1:])
    
    return street_address, postal_code, city

def load_data_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for entry in data:
        address = entry.get('address') 
        if address:
            street_address, postal_code, city = process_address(entry.get('address', ''))
            lab = Laboratory(
                place_id=entry.get('place_id', ''),
                name=entry.get('name', ''),
                description=entry.get('description'),
                is_spending_on_ads=entry.get('is_spending_on_ads', False),
                reviews=entry.get('reviews'),
                website=entry.get('website', ''),
                featured_image=entry.get('featured_image', ''),
                main_category=entry.get('main_category', ''),
                categories=entry.get('categories', []),
                rating=entry.get('rating'),
                workday_timing=entry.get('workday_timing', ''),
                closed_on=entry.get('closed_on', []),
                phone=entry.get('phone', ''),
                address=entry.get('address', ''),
                review_keywords=entry.get('review_keywords', []),
                link=entry.get('link', ''),
                owner=entry.get('owner', {}),
                street_address=street_address,
                postal_code=postal_code,
                city=city
            )
            lab.save()




@require_http_methods(['GET', 'POST'])  # Akceptuj tylko metody GET i POST
def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file_field')  # Pobierz listę plików

        # Ogranicz do maksymalnie 10 plików
        if len(files) > 10:
            print(len(files))
            return JsonResponse({'error': 'Można przesłać maksymalnie 10 plików.'}, status=400)

        for file in files:
            if file.name.endswith('.json'):
                file_path = default_storage.save('tmp/' + file.name, file)
                full_file_path = settings.MEDIA_ROOT + '/' + file_path
                load_data_from_json(full_file_path)
                default_storage.delete(file_path)  # Usuń plik po przetworzeniu
            else:
                return JsonResponse({'error': 'Niewłaściwy format pliku. Proszę przesłać plik JSON.'}, status=400)

        return JsonResponse({'message': 'Pliki zostały pomyślnie przetworzone.'})
    else:
        # Dla żądania GET, wyświetl formularz
        return render(request, 'upload.html')
    

class LaboratoryListCreate(generics.ListCreateAPIView):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer

class LaboratoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer

def index(request):
    return render(request, 'index.html')