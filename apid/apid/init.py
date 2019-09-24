def __init__(hub):
    print('apid works!')
    hub.pop.conf.integrate('apid', cli='apid', roots=True)
    hub.apid.init.validate_config()
    hub.apid.init.load_subs()


def load_subs(hub):
    '''
    Load up the needed subs
    '''
    # TODO? Does salt the aws module import apid, or does apid load the aws module
    # TODO? Based on the profile that's configured
    # hub.pop.sub.add('heis')
    # hub.pop.sub.add(dyne_name='idem')
    # hub.pop.sub.add(dyne_name='rend')


def validate_config(hub):
    assert hub.OPT['apid']['profile'], 'No profiles configured'
    assert hub.OPT['apid']['provider'], 'No providers configured'
