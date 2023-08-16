from django.contrib import admin
from .models import Branch
from .models import District,ApplicationForm,Team,Services

# Register your models here.


admin.site.register(District)
admin.site.register(Branch)
admin.site.register(ApplicationForm)
admin.site.register(Team)
admin.site.register(Services)