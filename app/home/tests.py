from django.test import TestCase
from django.contrib.auth.models import User
from .models import Account, Tree, PlantedTree
from decimal import Decimal

class TreePlantingTestCase(TestCase):

    def setUp(self):
        # Criar árvores
        tree1 = Tree.objects.create(name="Árvore 1", scientific_name="Arvore Unum")
        tree2 = Tree.objects.create(name="Árvore 2", scientific_name="Arvore Duo")

        # Criar contas
        account1 = Account.objects.create(name="Conta1")
        account2 = Account.objects.create(name="Conta2")

        # Criar usuários
        user1 = User.objects.create_user('user1', 'user1@example.com', 'user1password')
        user2 = User.objects.create_user('user2', 'user2@example.com', 'user2password')
        user3 = User.objects.create_user('user3', 'user3@example.com', 'user3password')

        account1.users.add(user1, user2)
        account2.users.add(user3)

        # Plantar árvores
        PlantedTree.objects.create(user=user1, tree=tree1, account=account1, latitude=Decimal('10.000000'), longitude=Decimal('10.000000'))
        PlantedTree.objects.create(user=user2, tree=tree2, account=account1, latitude=Decimal('20.000000'), longitude=Decimal('20.000000'))
        PlantedTree.objects.create(user=user3, tree=tree1, account=account2, latitude=Decimal('30.000000'), longitude=Decimal('30.000000'))
        
        
    def test_user_tree_list_template(self):
        self.client.login(username='user1', password='user1password')
        response = self.client.get('/planted-trees/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Árvore 1")
        self.assertNotContains(response, "Árvore 2")
        
    def test_access_other_user_tree_list(self):
        self.client.login(username='user1', password='user1password')
        response = self.client.get('/planted-trees/?user_id=3')
        self.assertEqual(response.status_code, 403)
        
    def test_account_tree_list_template(self):
        self.client.login(username='user1', password='user1password')
        response = self.client.get('/account-trees/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Árvore 1")
        self.assertContains(response, "Árvore 2")
        self.assertNotContains(response, "Árvore de outro usuário")
        
    def test_plant_tree_method(self):
        user = User.objects.get(username="user1")
        tree = Tree.objects.first()
        latitude = '40.000000'
        longitude = '-70.000000'
        user.plant_tree(tree, latitude, longitude)
        self.assertTrue(PlantedTree.objects.filter(user=user, latitude=Decimal(latitude), longitude=Decimal(longitude)).exists())

    def test_plant_trees_method(self):
        user = User.objects.get(username="user1")
        tree = Tree.objects.first()
        tree_locations = [(tree, ('50.000000', '-80.000000'))]
        user.plant_trees(tree_locations)
        self.assertTrue(PlantedTree.objects.filter(user=user, latitude=Decimal('50.000000'), longitude=Decimal('-80.000000')).exists())