#!/usr/bin/env python3

import yaml

with open('users_key.yml') as all_users:
    infra_users_access = yaml.safe_load(all_users)
    for user in infra_users_access['users']:
        keys = user.get('ssh_pubkeys', []) + user.get('ssh_revokedkeys', [])
        print("Revoked SSH keys: ")
        for key in set(keys):
            print(key)
    print("Staled SSH keys: ")
    for revoked_key in infra_users_access['users_ssh_keys_staled']:
        print(revoked_key)