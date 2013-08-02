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
from django.conf.urls import patterns, include, url

from admin.models import register_admin_models
from django.contrib import admin

admin.autodiscover()
register_admin_models()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'chaoscowboy.views.status', name='status'),
    url(r'^status.html', 'chaoscowboy.views.status', name='status'),
    url(r'^actions.html', 'chaoscowboy.views.actions', name='actions'),
    url(r'^action_groups.html', 'chaoscowboy.views.action_groups', name='action_groups'),
    url(r'^scheduling.html', 'chaoscowboy.views.scheduling', name='scheduling'),
    url(r'^reporting.html', 'chaoscowboy.views.reporting', name='reporting'),
    url(r'^settings.html', 'chaoscowboy.views.settings', name='settings'),
    # url(r'^ChaosCowboy/', include('ChaosCowboy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
