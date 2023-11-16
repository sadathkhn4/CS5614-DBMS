# populate_images.py
import os
from django.core.management.base import BaseCommand
from classifier.models import Image, Color, Category, COLOR_TYPE, CATEGORY_TYPE  # Replace 'yourapp' with the name of your Django app

class Command(BaseCommand):
    help = 'Populate the Image model with relative image paths'

    def handle(self, *args, **options):

        # iterate through the color_type and save values to the Color model
        for id, description in COLOR_TYPE:
            Color.objects.create(id=id, color_description=description)    

        # iterate through the category_type and save values to the Category model
        for id, description in CATEGORY_TYPE:
            Category.objects.create(id=id, category_description=description)    

        image_folder = 'C:\\Utility\\CGIT Rep\\CS5614-DBMS\\100_Images'  # Replace with the actual path
        image_folder_relative = "100_Images"

        for filename in os.listdir(image_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust based on your image file types
                Image.objects.create(path=filename)    
                self.stdout.write(self.style.SUCCESS(f'Successfully added image: {filename}'))    
        


        # for i in range(100):
        #     relative_path = f'{i:02d}.jpg'
        #     #path = os.path.join(image_folder, relative_path)
        #     #Image.objects.create(path=relative_path)
        #     #self.stdout.write(self.style.SUCCESS(f'Successfully added image: {relative_path}'))
            
    



            