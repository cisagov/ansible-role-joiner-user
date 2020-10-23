# ansible-role-joiner-user #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-joiner-user/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-joiner-user/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-joiner-user.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-joiner-user/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-joiner-user.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-joiner-user/context:python)

This Ansible role creates the `joiner` user, whose sole reason for
existence is to join the host to the
[FreeIPA](https://www.freeipa.org/) domain.

## Requirements ##

None.

## Role Variables ##

None.

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - joiner
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

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
