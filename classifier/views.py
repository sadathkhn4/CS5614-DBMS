from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from classifier.models import Map 
from classifier.models import Image 
import uuid, random

def streamlit_app(request):
    # Run the Streamlit app as a subprocess
    subprocess.run(["streamlit", "run", "app5.py"])
    return HttpResponse("Streamlit app is running.")


# def index(request):
#     return render(request, 'index.html')

def streamlit_app2(request):
    # Run the Streamlit app as a subprocess
    subprocess.run(["streamlit", "run", "app7.py"])
    return HttpResponse("Streamlit app-2 is running.")

def index(request):
    # Get the image_number parameter from the URL
    category_value = request.GET.get('predicted_category')

    rows_with_category = Map.objects.filter(category=category_value)

    # for row in rows_with_category:
    #     id_value = row.id
    #     image_number_jpg =  Image.objects.filter(id=id_value)

    # Validate and process the image_number
    if category_value is not None and category_value.isdigit():
        #image_path = f'path/to/images/image_{image_number}.jpg'  # Replace with your actual image path
        image_path=""

        results = [] 

        for row in rows_with_category:
            id_uuid = row.id.id
            #dummy_id = "465ef864-834a-435f-99f9-f84f6741fb3f"
            image_number_jpg =  Image.objects.filter(id=id_uuid)
            for x in image_number_jpg:
                image_path = "../static/img/"
                image_path = image_path +  f"{x.path}"
                results.append(image_path)
            
            random_5_images_cat  = [results[i] for i in random.sample(range(len(results)), min(5, len(results)))]
                
        
        return render(request, 'index2.html', {'results': random_5_images_cat})
    else:
        return HttpResponse("Invalid image_number provided in the URL.")
