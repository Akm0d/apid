CLI_CONFIG = {
    'user': {
        'default': 'root',
        'type': str,
        'help': 'The salt master user',
    },
    'profile': {
        'default': None,
        'action': 'append',
        'help': 'The absolute path to a cloud profile config',
    },
    'provider': {
        'default': None,
        'action': 'append',
        'help': 'The absolute path to a cloud provider config',
    },
    'maps': {
        'default': None,
        'help': 'The map dict from pillars'
    },
    'list_images': {
        'action': 'store_true',
    },
    'list_locations': {
        'action': 'store_true',
    },
    'list_profiles': {
        'action': 'store_true',
    },
    'list_providers': {
        'action': 'store_true',
    },
    'list_sizes': {
        'action': 'store_true',
    },
    'action': {
    },
    'destroy': {
        'action': 'store_true',
    },
    'function': {
        'action': 'store_true',
    },
}

CONFIG = {}
GLOBAL = {}
SUBS = {}
