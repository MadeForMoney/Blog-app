from blog.models import Category
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help='For inserting post category'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        
        category_list=['Technology','Art','Food','Science','Sports']


        for name in category_list:
            Category.objects.create(name=name)

        self.stdout.write(self.style.SUCCESS("completed data insertion!"))