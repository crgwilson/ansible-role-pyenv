# Ansible role: pyenv

![Molecule Test](https://github.com/crgwilson/ansible-role-pyenv/workflows/Molecule%20Test/badge.svg)

Install [pyenv](https://github.com/pyenv/pyenv) and pyenv plugins

* Install packages necessary to build Python from source
* Clone the pyenv source from git
* Clone pyenv plugins from git

## Variables

Most variables for this role are pretty straight forward, except one...

### pyenv_plugins

`pyenv_plugins` is a dictionary containing info required to install plugins for pyenv.
By default this is set to install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

The dict is expected to be formatted as follows...

```yaml
pyenv_plugin_info:
  plugin-name:
    source_uri: https://github.com/foo/bar.git
    version: git-ref
```

## Usage

This role only installs `pyenv`. If you want to use it check out step 2 of
[the pyenv install guide](https://github.com/pyenv/pyenv#basic-github-checkout)

In short, you need the below two environment variables set in your shell...

```bash
export PYENV_ROOT="/usr/local/pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
```

## Testing

Testing for this project is setup using
[Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```

## Dependencies

* [ansible-role-git](https://github.com/crgwilson/ansible-role-git)
