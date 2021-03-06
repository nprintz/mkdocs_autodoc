from mkdocs import events

from .nav import load_module
from . import build, config as ext_config

def main(event):
    if event.cmd == 'autodoc-generate':
        modules = [arg for arg in event.args if not arg.startswith('--')]
        base_path = event.options.get('basepath', 'api')
        out_path = event.options.get('outpath', './docs/api')

        for module_name in modules:
            page = load_module(module_name, base_path)
            page.export_markdown(out_path)

        event.consumed = True

def init_extension(config):
    """
    Initializes the extension for the mkdocs system.

    ### Parameters
        config | <dict>
    """
    # update the configuration options
    ext_config.update(config.get('autodoc_options', {}))
    ext_config.base_config = config

    # register callback options
    events.register_callback(events.BuildPage, build.create_api_page)
    events.register_callback(events.GenerateContent, build.create_api_content)
    events.register_callback(events.CLI, main)

    # register the additional command line option
    events.CLI.commands.add('autodoc-generate')