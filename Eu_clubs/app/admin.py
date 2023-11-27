from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'std_id', 'message')
    
    
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'std_id','club', 'email', 'image')
    
class MemberAdmin(admin.ModelAdmin):
    list_display = ('mem_name', 'std_id','club', 'position')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Member, MemberAdmin)