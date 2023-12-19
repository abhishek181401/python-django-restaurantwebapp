from django.contrib import admin
from .models import Recipe,Owner,ContactNumber,TeamMember,UserQuery

admin.site.site_header = "Everest Momo Admin"

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display =['name','price','type']
    search_fields= ('name',)

admin.site.register(Recipe,RecipeAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display =['location','restaurantname']

admin.site.register(Owner,OwnerAdmin)


class TeamMemberAdmin(admin.ModelAdmin):
    list_display =['name','position']

admin.site.register(TeamMember,TeamMemberAdmin)


class ContactNumberAdmin(admin.ModelAdmin):
    list_display =['number']

admin.site.register(ContactNumber,ContactNumberAdmin)

class UserQueryAdmin(admin.ModelAdmin):
    list_display =['firstname','phone_number','email','service','message']

admin.site.register(UserQuery,UserQueryAdmin)