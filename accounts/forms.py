from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):  
  #Metaクラスをオーバーライド。教科書は細字だがこれがないとメールアドレス入力枠がでない
  class Meta:
    model = CustomUser
    fields = ('username', 'email', 'password1', 'password2')