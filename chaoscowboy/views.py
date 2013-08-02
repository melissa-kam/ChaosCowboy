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
from django.http import HttpResponse
import pyrax

pyrax.set_setting("identity_type", "rackspace")

def home(request):
    pyrax.set_credentials(request.user.rax_username, request.user.rax_api_key)

    cs_dfw = pyrax.connect_to_cloudservers(region="DFW")
    cs_ord = pyrax.connect_to_cloudservers(region="ORD")

    dfw_servers = cs_dfw.servers.list()
    ord_servers = cs_ord.servers.list()
    all_servers = dfw_servers + ord_servers

    html = "<html><body>"

    for server in all_servers:
        html += "Server: %s <br/>" % server.name

    html += "</body></html>"

    return HttpResponse(html)