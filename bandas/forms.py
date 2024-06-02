from django import forms
from .models import Banda, Album, Musica

class EditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        item_type = kwargs.pop('item_type', None)
        super(EditForm, self).__init__(*args, **kwargs)
        if item_type:
            if item_type == 'album':
                self._meta.model = Album
                self.fields = {field.name: forms.ModelChoiceField(queryset=field.related_model.objects.all()) if field.many_to_one else forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})) for field in Album._meta.fields}
            elif item_type == 'musica':
                self._meta.model = Musica
                self.fields = {field.name: forms.ModelChoiceField(queryset=field.related_model.objects.all()) if field.many_to_one else forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})) for field in Musica._meta.fields}
            elif item_type == 'banda':
                self._meta.model = Banda
                self.fields = {field.name: forms.ImageField() if field.name == 'foto' else forms.ModelChoiceField(queryset=field.related_model.objects.all()) if field.many_to_one else forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})) for field in Banda._meta.fields}

    class Meta:
        model = Banda
        fields = ['nome', 'foto', 'descricao', 'pais_origem', 'genero', 'data_formacao']
        help_texts = {
            'nome': 'Insira o nome da banda.',
            'foto': 'Faça upload de uma foto da banda.',
            'descricao': 'Insira uma descrição detalhada da banda.',
            'pais_origem': 'Insira o país de origem da banda.',
            'genero': 'Insira o gênero musical da banda.',
            'data_formacao': 'Insira a data de formação da banda (formato: AAAA-MM-DD).'
        }