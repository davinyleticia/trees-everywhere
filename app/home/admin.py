from django.contrib import admin
from .models import Account, Profile, Tree, PlantedTree

# Admin para o modelo Account
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'active')

admin.site.register(Account, AccountAdmin)

# Admin para o modelo Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'joined')

admin.site.register(Profile, ProfileAdmin)

# Admin para o modelo Tree
class TreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')

admin.site.register(Tree, TreeAdmin)

# Admin para o modelo PlantedTree
class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ('tree', 'user', 'age', 'planted_at', 'latitude', 'longitude', 'account')

admin.site.register(PlantedTree, PlantedTreeAdmin)