from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .forms import EditForm
from .models import Album, Banda, Musica
# Create your views here.

def home_view(request):
    albuns = Album.objects.all()
    bandas = Banda.objects.all()
    context = {
        'albuns': albuns,
        'bandas': bandas,
    }
    return render(request, 'bandas/home.html', context)

def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {
        'album': album,
    }
    return render(request, 'bandas/album.html', context)

def banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    context = {
        'banda': banda,
    }
    return render(request, 'bandas/banda.html', context)

def musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    context = {
        'musica': musica,
    }
    return render(request, 'bandas/musica.html', context)


def user_is_editor(user):
    return user.groups.filter(name='editores de bandas').exists()

@login_required
@user_passes_test(user_is_editor)
def edit_item(request, item_id, item_type):
    if not request.user.is_authenticated:
        # Redirect unauthenticated users to the external login page
        return redirect('https://a21807126.pythonanywhere.com/autenticacao/login/?next=/bandas/editar/{}/{}/'.format(item_type, item_id))
    if item_type == 'banda':
        item = Banda.objects.get(pk=item_id)
    elif item_type == 'album':
        item = Album.objects.get(pk=item_id)
    elif item_type == 'musica':
        item = Musica.objects.get(pk=item_id)

    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, item_type=item_type)
        if form.is_valid():
            form.save()
            if item_type == 'banda':
                return redirect('https://a21807126.pythonanywhere.com/bandas/banda/{}/'.format(item.id))
            elif item_type == 'album':
                return redirect('https://a21807126.pythonanywhere.com/bandas/album/{}/'.format(item.id))
            elif item_type == 'musica':
                return redirect('https://a21807126.pythonanywhere.com/bandas/musica/{}/'.format(item.id))
    else:
        form = EditForm(request.POST, item_type=item_type)
    return render(request, 'bandas/editar_form.html', {'form': form, 'item_type': item_type})


@login_required
@user_passes_test(user_is_editor)
def create_item(request, item_type):
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, item_type=item_type)
        item_type = request.POST.get('item_type')
        if form.is_valid():
            item = form.save()
            if item_type == 'banda':
                return redirect('https://a21807126.pythonanywhere.com/bandas/banda/{}/'.format(item.id))
            elif item_type == 'album':
                return redirect('https://a21807126.pythonanywhere.com/bandas/album/{}/'.format(item.id))
            elif item_type == 'musica':
                return redirect('https://a21807126.pythonanywhere.com/bandas/musica/{}/'.format(item.id))
    else:
        form = EditForm(request.POST, item_type=item_type)
    return render(request, 'bandas/criar_form.html', {'form': form, 'item_type': item_type})

def html5css_view(request):

    return render(request, 'bandas/html5-css.html')