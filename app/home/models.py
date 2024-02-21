from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


# Template for account, which can group multiple users
class Account(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    created = models.DateTimeField(auto_now_add=True, verbose_name="criado em")
    active = models.BooleanField(default=True, verbose_name="ativo")
    users = models.ManyToManyField(User, related_name='accounts', verbose_name="usuários")

    def __str__(self):
        return self.name


# Template for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="usuário")
    about = models.TextField(blank=True, verbose_name="sobre")
    joined = models.DateTimeField(auto_now_add=True, verbose_name="entrou em")


# Template for tree
class Tree(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    scientific_name = models.CharField(max_length=255, verbose_name="Nome científico")

    def __str__(self):
        return self.name


# Template for planted trees
class PlantedTree(models.Model):
    age = models.IntegerField(default=0, verbose_name="idade")
    planted_at = models.DateTimeField(auto_now_add=True, verbose_name="plantado em")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="usuário")
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, verbose_name="árvore")
    account = models.ForeignKey(Account, on_delete=models.CASCADE,  verbose_name="conta")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="longitude")


# Adding methods to the User model
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


User.add_to_class('plant_tree', lambda self, tree, latitude, longitude, age, account:
    PlantedTree.objects.create(
        user=self,
        tree=tree,
        latitude=Decimal(latitude),
        longitude=Decimal(longitude),
        age=age,
        account=account
    )
)
