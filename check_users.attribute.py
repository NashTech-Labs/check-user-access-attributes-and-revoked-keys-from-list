#!/usr/bin/env python3

import yaml

with open('users_key.yml') as all_users:
    infra_users_access = yaml.safe_load(all_users)
    attributes = set()
    for user in infra_users_access['users']:
        attributes.update(user)

    unexpected = attributes - set([
        "name",
        "description",
        "uid",
        "group",
        "ssh_revokedkeys",
        "ssh_pubkeys",
        "ssh_pubkeys_dev",
        # can add more attributes like ssh keys for different environments.
    ])
    assert not unexpected, "At least one unexpected attribute was found: %r" % unexpected