from django import forms
from django.utils import timezone
from .models import Comment, Post

class EditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        item_type = kwargs.pop('item_type', None)
        post_instance = kwargs.pop('post_instance', None)  # Pop post_instance from kwargs if present
        self.user = kwargs.pop('user', None)  # Store user from kwargs if present
        super(EditForm, self).__init__(*args, **kwargs)
        
        if item_type == 'comment':
            self.instance = Comment()  # Change instance to Comment
            self._meta.model = Comment
            self.fields = {
                field.name: forms.ModelChoiceField(queryset=field.related_model.objects.all()) if field.many_to_one else forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})) 
                for field in Comment._meta.fields 
                if field.name not in ['id', 'post', 'created_at', 'author']
            }
            # Set post field with given post_instance
            if post_instance:
                self.fields['post'] = forms.ModelChoiceField(queryset=Post.objects.filter(id=post_instance.id), initial=post_instance, widget=forms.HiddenInput())
        
        elif item_type == 'post':
            self.instance = Post()  # Change instance to Post
            self._meta.model = Post
            self.fields = {
                field.name: forms.ImageField() if field.name == 'cover_image' else forms.ModelChoiceField(queryset=field.related_model.objects.all()) if field.many_to_one else forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})) 
                for field in Post._meta.fields 
                if field.name not in ['id', 'created_at', 'author']
            }

    def save(self, commit=True):
        # Automatically set created_at and author
        if self.instance._meta.model == Comment:
            self.instance.created_at = timezone.now()
            if self.user:
                self.instance.author = self.user
        
        elif self.instance._meta.model == Post:
            self.instance.created_at = timezone.now()
            if self.user:
                self.instance.author = self.user

        return super(EditForm, self).save(commit=commit)

    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'cover_image']
