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
from chaoscowboy.models import ActionTemplate
from django.http import HttpResponse
from django.template import RequestContext, loader
import pyrax

pyrax.set_setting("identity_type", "rackspace")

def status(request):
    template = loader.get_template('status.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def actions(request):
    template = loader.get_template('actions.html')
    actions = ActionTemplate.objects.all()
    context = RequestContext(request, {
        'actions': actions
    })
    return HttpResponse(template.render(context))

def action_groups(request):
    template = loader.get_template('action_groups.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def scheduling(request):
    template = loader.get_template('scheduling.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def reporting(request):
    template = loader.get_template('reporting.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def settings(request):
    template = loader.get_template('settings.html')
    username = request.user.rax_username
    api_key = request.user.rax_api_key
    context = RequestContext(request, {
        'username': username,
        'key': api_key
    })
    return HttpResponse(template.render(context))


def home(request):
    pyrax.set_credentials(request.user.rax_username, request.user.rax_api_key)

    cs_dfw = pyrax.connect_to_cloudservers(region="DFW")
    cs_ord = pyrax.connect_to_cloudservers(region="ORD")

    dfw_servers = cs_dfw.servers.list()
    ord_servers = cs_ord.servers.list()
    all_servers = dfw_servers + ord_servers

    html = "<html><body>"

    for server in all_servers:
        html += "Server: {0} ({1}) <br/>".format(server.name, server.status)

    html += "</body></html>"

    return HttpResponse(html)
