from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PlantedTree, Tree
from .forms import PlantedTreeForm, TreeForm, AccountForm, UserCreateForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import PlantedTreeSerializer


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('planted_trees')
        else:
            return render(request, 'login.html', {'error': 'nome de usuário ou senha inválidos.'})
    else:
        return render(request, 'login.html')

@login_required
def planted_trees(request):
    trees = PlantedTree.objects.filter(user=request.user)
    return render(request, 'planted_trees.html', {'trees': trees})

@login_required
def planted_tree_detail(request, tree_id):
    tree = get_object_or_404(PlantedTree, id=tree_id, user=request.user)
    return render(request, 'planted_tree_detail.html', {'tree': tree})

@login_required
def add_planted_tree(request):
    if request.method == 'POST':
        form = PlantedTreeForm(request.POST)
        if form.is_valid():
            planted_tree = form.save(commit=False)
            planted_tree.user = request.user
            planted_tree.save()
            return redirect('planted_trees')
    else:
        form = PlantedTreeForm()
    return render(request, 'add_planted_tree.html', {'form': form})

@login_required
def account_trees(request):
    # Obter todas as PlantedTrees que estão associadas ao usuário logado.
    planted_trees = PlantedTree.objects.filter(user=request.user).select_related('account').distinct()
    # Cria um conjunto de contas únicas dessas árvores plantadas.
    accounts = {tree.account for tree in planted_trees}
    
    # Agora, se você quer todas as árvores plantadas nessas contas, faça outra consulta.
    all_trees_in_accounts = PlantedTree.objects.filter(account__in=accounts).distinct()
    
    return render(request, 'account_trees.html', {'planted_trees': all_trees_in_accounts})



@login_required
def add_tree(request):
    if request.method == 'POST':
        form = TreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planted_trees')  # Substitua por sua URL de listagem de árvores
    else:
        form = TreeForm()
    return render(request, 'add_tree.html', {'form': form})

@login_required
def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planted_trees')  # Substitua por sua URL de listagem de contas
    else:
        form = AccountForm()
    return render(request, 'add_account.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('/')  # Redirect to a desired page
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redireciona para a página de login ou para a home page após o logout
    return redirect('/')  # Substitua 'login' pelo nome da URL para a qual você quer redirecionar


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class PlantedTreesListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        trees_planted_by_user = PlantedTree.objects.filter(user=user)
        serializer = PlantedTreeSerializer(trees_planted_by_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

