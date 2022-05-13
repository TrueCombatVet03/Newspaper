from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Title,Author,Body

from accounts.forms import CustomUserCreationForm


from .models import CustomUser, UserType, Language
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email', 'username',
        'user_type', 'preferred_language',
        'is_staff' 
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields': ('user_type', 'preferred_language')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('user_type', 'preferred_language')}),
    )


class AuthorAdmin(UserAdmin):
    model = CustomUser
    list_display = ('Frontpage', 'Sports', 'Society', 'Buisness')


class TitleAdmin(UserAdmin):
    model = CustomUser
    list_display = ('title', 'author', 'display_genre')

class BodyAdmin(UserAdmin):
    pass









admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType)
admin.site.register(Language)
admin.site.register(Author )
admin.site.register(Title)

admin.site.register(Body)


