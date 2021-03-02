from django.contrib import admin
from .models import Media, MyUser, Notes, CheckBox
# Register your models here.

admin.site.register(Media)
admin.site.register(MyUser)
admin.site.register(Notes)
admin.site.register(CheckBox)
