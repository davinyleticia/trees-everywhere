# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from .models import Account, Profile, Tree, PlantedTree

# # Admin para o modelo Profile
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'

# # Definindo um novo User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline, )
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'account')

#     def account(self, instance):
#         # Esta função é para mostrar a conta associada ao usuário, se houver
#         accounts = instance.account_set.all()
#         if accounts:
#             return ', '.join([account.name for account in accounts])
#         return None

# # Re-registra o modelo User
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# # Admin para o modelo Account
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created', 'active')
#     list_filter = ('active',)
#     actions = ['make_active', 'make_inactive']

#     def make_active(self, request, queryset):
#         queryset.update(active=True)

#     make_active.short_description = "Ativar contas selecionadas"

#     def make_inactive(self, request, queryset):
#         queryset.update(active=False)

#     make_inactive.short_description = "Desativar contas selecionadas"

# admin.site.register(Account, AccountAdmin)

# # Admin para o modelo Tree
# class TreeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'scientific_name')

# admin.site.register(Tree, TreeAdmin)

# # Admin para o modelo PlantedTree
# class PlantedTreeAdmin(admin.ModelAdmin):
#     list_display = ('tree', 'user', 'age', 'planted_at', 'location')
#     readonly_fields = ('location',)

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         queryset = queryset.prefetch_related('tree', 'user')
#         return queryset

# admin.site.register(PlantedTree, PlantedTreeAdmin)




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