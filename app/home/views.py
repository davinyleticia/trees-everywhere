from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PlantedTree, Tree, Profile
from .forms import PlantedTreeForm, TreeForm, AccountForm, UserCreateForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import PlantedTreeSerializer



# Page Login
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
    
# Page Planted Trees
@login_required
def planted_trees(request):
    trees = PlantedTree.objects.filter(user=request.user)
    return render(request, 'planted_trees.html', {'trees': trees})

# Page Planted Tree Detail
@login_required
def planted_tree_detail(request, tree_id):
    tree = get_object_or_404(PlantedTree, id=tree_id, user=request.user)
    return render(request, 'planted_tree_detail.html', {'tree': tree})

# Page Add Planted Tree
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

# Page Account Trees
@login_required
def account_trees(request):
    
    planted_trees = PlantedTree.objects.filter(user=request.user).select_related('account').distinct()
    
    accounts = {tree.account for tree in planted_trees}
    
    all_trees_in_accounts = PlantedTree.objects.filter(account__in=accounts).distinct()
    
    return render(request, 'account_trees.html', {'planted_trees': all_trees_in_accounts})


# Page Add Tree
@login_required
def add_tree(request):
    if request.method == 'POST':
        form = TreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planted_trees')
    else:
        form = TreeForm()
    return render(request, 'add_tree.html', {'form': form})

# Page Add Account
@login_required
def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planted_trees') 
    else:
        form = AccountForm()
    return render(request, 'add_account.html', {'form': form})


@login_required
def profile_detail_view(request):
    
    # Recupera o perfil associado ao usuário atual
    profile = get_object_or_404(Profile, user=request.user)
    
    return render(request, 'profile_detail.html', {'profile': profile})

# Page Register
def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('/')  

# API Planted Trees List
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

# API Planted Trees List
class PlantedTreesListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        trees_planted_by_user = PlantedTree.objects.filter(user=user)
        serializer = PlantedTreeSerializer(trees_planted_by_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

