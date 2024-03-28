# ansible-role-joiner-user #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-joiner-user/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-joiner-user/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-joiner-user/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-joiner-user/actions/workflows/codeql-analysis.yml)

This Ansible role creates the `joiner` user, whose sole reason for
existence is to join the host to the
[FreeIPA](https://www.freeipa.org/) domain.

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

- [cisagov/ansible-role-freeipa-client](https://github.com/cisagov/ansible-role-freeipa-client):
  In order to join a host to a FreeIPA domain, one must have the
  FreeIPA client system package installed.

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: skeleton
  src: https://github.com/cisagov/skeleton-ansible-role
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Create the joiner user
      ansible.builtin.include_role:
        name: joiner_user
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
