from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from testblog.models import Comments, Posts

class UserLoginForm(forms.Form):
    username = forms.CharField(label=_(u'Username'), max_length=30)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('postname','post','permission')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)

class ChangeProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

# Creating a form to add an article.
#form = RegisterForm()

# Creating a form to change an existing article.
#article = Article.objects.get(pk=1)
#form = ArticleForm(instance=article)
