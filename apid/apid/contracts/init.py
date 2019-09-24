from typing import Any, Dict


# This is where 'salt-cloud' execution modules are contracted
# Every cloud provider must implement these functions with these parameters


def sig_create(hub, vm_: Dict[str, Any]):
    '''
    Create a single VM from a data dict
    '''


def pre_create(hub, ctx):
    pass


def post_create(hub, ctx):
    pass


def sig_destroy(hub, name: str):
    '''
    Destroy a node. Will check termination protection and warn if enabled.
    '''


def sig_list_nodes(hub):
    '''
    Return a list of the VMs that are on the provider
    '''


def sig_list_nodes_full(hub, location: str = None):
    '''
    Return a list of the VMs that are on the provider
    '''


def sig_list_nodes_select(hub):
    '''
    Return a list of the VMs that are on the provider, with select fields
    '''


def sig_show_instance(
        hub,
        name: str = None,
        instance_id: str = None,
        **kwargs):
    '''
    Show the details from the provider concerning an instance.
    '''
