import re
import importlib

from aiohttp import web
from server import PromptServer

from nodes import load_custom_node

routes = PromptServer.instance.routes

@routes.get("/node_dev/reload/{module_name}")
async def reload(request):
    """ Reload the requested custom node """
    module_name = request.match_info['module_name']
    if not re.match('^[0-9A-Za-z_-]+$', module_name):
        return web.Response(text='Invalid module name', status=400)

    # ensure the module is reloaded
    module = importlib.import_module(module_name)
    load_custom_node('custom_nodes/' + module_name)
    return web.Response(text='OK') #headers={'Location': '/'})


