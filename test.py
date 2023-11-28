from classifier.models import Map  # Replace 'yourapp' with the name of your Django app

def display_ids_for_category_3():
    category_value = 3
    rows_with_category_3 = Map.objects.filter(category=category_value)

    for row in rows_with_category_3:
        print(f"ID: {row.id}")

# Call the function
display_ids_for_category_3()
