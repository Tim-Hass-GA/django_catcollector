from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat, Toy
from .forms import CatForm, LoginForm, SignUpForm, ToyForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import requests
# test the HttpResponse with simple string
# post creates a need for a redirect

# Create your views here.
#  “index” page – displays the home view.
#  “detail” page – displays a question text, with no results but with a form to vote.
#  “results” page – displays results for a particular item.
#  action – handles action for a particular choice in a particular question.
#  example template should be at polls/templates/polls/index.html

# TEST DATA
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
#
# cats = [
#     Cat('Loki','tabby', 'some info about Loki', 3),
#     Cat('Brian','Dobbie', 'My best buddy', 9),
#     Cat('Tiny','tabby', 'some info about Tiny', 4),
#     Cat('Scratchy','clawy', 'some info about Scratchy', 3),
#     Cat('Johny','fuzzy', 'some info about Johnny', 0)
# ]

##### GET HOME ROUTE
def index(request):
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, 'index.html', {'cats':cats, 'form':form})
    # render(request template context)

##### SHOW CAT ROUTE
def show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    form = ToyForm()
    # payload = {'key':'TOKEN'}
    res = requests.get('http://thecatapi.com/api/images/get')
    # res = requests.get('http://thecatapi.com/api/images/get', params=payload)
    # return render(request, 'api.html', {'imageurl':res.url})
    return render(request, 'show.html', {'cat':cat, 'form':form, 'imageurl':res.url})

##### CREATE CAT ROUTE
def post_cat(request):
    form = CatForm(request.POST)
    # method on the form object
    if form.is_valid():
        #     cat = Cat(
        #         name = form.cleaned_data['name'],
        #         description = form.cleaned_data['description'],
        #         breed = form.cleaned_data['breed'],
        #         age = form.cleaned_data['age']
        #     )
        cat = form.save(commit = False)
        cat.user = request.user
        cat.save()
    return HttpResponseRedirect('/')

##### PROFILE ROUTE
def profile(request, user_name):
    user = User.objects.get(username=user_name)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username':user_name, 'cats':cats})

##### LOGIN ROUTE
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("This account has been disabled.")
                    return render(request, 'signup.html', {
                        'form':form,
                        'error_message': "This account has been disabled."
                    })
            else:
                print("The username and or password is incorrect.")
                # redisplay the login form
                return render(request, 'login.html', {
                    'form':form,
                    'error_message': "The username and or password is incorrect."
                })
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

##### LOG OUT ROUTE
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

##### SIGN UP ROUTE
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            print("Something when wrong in the sign up process")
            # redisplay the signup form
            return render(request, 'signup.html', {
                'form':form,
                'error_message': "Username or password doesn't match."
            })
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

##### LIKE CAT ROUTE
## TODO: add conditional for users ...............
def like_cat(request):
    cat_id = request.GET.get('cat_id', None)
    likes = 0
    if (cat_id):
        cat = Cat.objects.get(id=int(cat_id))
        if cat is not None:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()
    return HttpResponse(likes)

##### CAT PUT ROUTE
## TODO: add conditional for users ...............
def edit_cat(request, cat_id):
    instance = get_object_or_404(Cat, id=cat_id)
    form = CatForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('show', cat_id)
    return render(request, 'edit_cat.html', {'cat':instance, 'form':form})

##### CAT DELETE ROUTE
## TODO: add conditional for users ...............
def delete_cat(request, cat_id):
    if request.method == 'POST':
        instance = Cat.objects.get(pk=cat_id)
        instance.delete()
        return redirect('index')

##### CREATE TOY ROUTE
def create_toy(request, cat_id):
    form = ToyForm(request.POST)
    if form.is_valid():
        # if we have good POST data
        # see if there is a toy with this name
        try:
            toy = Toy.objects.get(name=form.data.get('name'))
        except:
            toy = None
        #if no toy by that name exists save it to the database
        if toy is None:
            toy = form.save()
        cat = Cat.objects.get(pk=cat_id)
        toy.cats.add(cat)
        return redirect('show_toy', toy.id)
    else:
        return redirect('show', cat_id)

##### SHOW TOY ROUTE
def show_toy(request, toy_id):
    toy = Toy.objects.get(pk=toy_id)
    cats = toy.cats.all()
    return render(request, 'show_toy.html', {'toy': toy, 'cats':cats})

### API ROUTE
# requests is a thing....for api calls
def api(request):
    # payload = {'key':'TOKEN'}
    res = requests.get('http://thecatapi.com/api/images/get')
    # res = requests.get('http://thecatapi.com/api/images/get', params=payload)
    return render(request, 'api.html', {'imageurl':res.url})
