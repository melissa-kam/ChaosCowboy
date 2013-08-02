"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm)

from chaoscowboy.models import CowboyUser


class CowboyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CowboyUser


# Having this class here *should* include 'rax_username' and 'rax_api_key' in
# the admin user creation form but due to the bug
# https://code.djangoproject.com/ticket/19353 those fields don't appear.
# Unfortunately the work around in that ticket wasn't working for me. So you
# have to create a user and then add 'rax_username' and 'rax_api_key' in the
# change user form. There's a good discussion on this at StackOverflow as well
# http://stackoverflow.com/questions/15012235
#     /using-django-auth-useradmin-for-a-custom-user-model
class CowboyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CowboyUser

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            CowboyUser.objects.get(username=username)
        except CowboyUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class CowboyUserAdmin(UserAdmin):
    form = CowboyUserChangeForm
    add_form = CowboyUserCreationForm

    fieldsets = (
            (None, {'fields': ('rax_username', 'rax_api_key',)}),
    ) + UserAdmin.fieldsets


admin.site.register(CowboyUser, CowboyUserAdmin)
