from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .forms import EditForm
from .models import Post, Comment

# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'artigos/home.html', context)

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'artigos/post.html', context)

def user_is_editor(user):
    return user.groups.filter(name='editores de artigos').exists()

@login_required
@user_passes_test(user_is_editor)
def edit_item(request, item_id, item_type):
    if not request.user.is_authenticated:
        # Redirect unauthenticated users to the external login page
        return redirect('https://a21807126.pythonanywhere.com/autenticacao/login/?next=/artigos/editar/{}/{}/'.format(item_type, item_id))
    if item_type == 'post':
        item = Post.objects.get(pk=item_id)
    elif item_type == 'comment':
        item = Comment.objects.get(pk=item_id)

    if request.method == 'POST':
        form = EditForm(request.POST or None, item_type=item_type)
        if form.is_valid():
            form.save()
            if item_type == 'post':
                return redirect('https://a21807126.pythonanywhere.com/artigos/post/{}/'.format(item.id))
            elif item_type == 'comment':
                return redirect('https://a21807126.pythonanywhere.com/artigos/post/{}/'.format(item.post.id))
    else:
        form = EditForm(request.POST or None, item_type=item_type)
    return render(request, 'artigos/editar_form.html', {'form': form, 'item_type': item_type})


@login_required(login_url='/autenticacao/login/')
@user_passes_test(user_is_editor)
def create_item(request, item_type):
    if request.method == 'POST':
        post_instance = None
        if item_type == 'comment':
            post_id = request.POST.get('post_id')  # Assumes post_id is passed in POST data
            post_instance = Post.objects.get(id=post_id)
        form = EditForm(request.POST, request.FILES, item_type=item_type, post_instance=post_instance, user=request.user)
        if form.is_valid():
            item = form.save()  # Specifically at this line!
            if item_type == 'post':
                return redirect('https://a21807126.pythonanywhere.com/artigos/post/{}/'.format(item.id))
            elif item_type == 'comment':
                return redirect('https://a21807126.pythonanywhere.com/artigos/post/{}/'.format(item.post.id))
    else:
        form = EditForm(item_type=item_type)
    return render(request, 'artigos/criar_form.html', {'form': form})  # Replace 'template_name.html' with your actual template