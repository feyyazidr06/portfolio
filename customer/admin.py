from django.contrib import admin
from .models import Musteri, Note, Company, Doc

# Register your models here.
admin.site.register(Musteri)
admin.site.register(Note)
admin.site.register(Company)
admin.site.register(Doc)