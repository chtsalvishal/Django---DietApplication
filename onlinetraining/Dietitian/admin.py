from django.contrib import admin

# import the new class
from .models import DietitianProfile
from .models import PracticeLocation
# Register your models here.

# we will register our new class.
admin.site.register(DietitianProfile)
admin.site.register(PracticeLocation)