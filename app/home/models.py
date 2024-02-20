from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Modelo para conta, que pode agrupar vários usuários
class Account(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name='accounts')

    def __str__(self):
        return self.name

# Modelo para o perfil do usuário
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    joined = models.DateTimeField(auto_now_add=True)

# Modelo para árvore
class Tree(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Modelo para árvores plantadas
class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

# Adicionando métodos no modelo User
User.add_to_class('plant_tree', lambda self, tree, latitude, longitude: 
                  PlantedTree.objects.create(
                      user=self, tree=tree,
                      latitude=Decimal(latitude), longitude=Decimal(longitude)
                  ))

User.add_to_class('plant_trees', lambda self, tree_locations: 
                  [PlantedTree.objects.create(
                      user=self, tree=tree_location[0],
                      latitude=Decimal(tree_location[1][0]), longitude=Decimal(tree_location[1][1])
                  ) for tree_location in tree_locations])