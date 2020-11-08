import pytest


DEBIAN_PACKAGE_LIST = [
    "make",
    "build-essential",
    "libssl-dev",
    "zlib1g-dev",
    "libbz2-dev",
    "libreadline-dev",
    "libsqlite3-dev",
    "wget",
    "curl",
    "llvm",
    "libncurses5-dev",
    "xz-utils",
    "tk-dev",
    "libxml2-dev",
    "libxmlsec1-dev",
    "libffi-dev",
    "liblzma-dev",
]

REDHAT_PACKAGE_LIST = [
    "gcc",
    "zlib-devel",
    "bzip2",
    "bzip2-devel",
    "readline-devel",
    "sqlite",
    "sqlite-devel",
    "openssl-devel",
    "tk-devel",
    "libffi-devel",
]

PYENV_COMMAND_PREFIX = "PATH=/usr/local/pyenv/shims:/usr/local/pyenv/bin:$PATH "


def test_default_packages(host):
    if host.system_info.distribution == "centos":
        package_list = REDHAT_PACKAGE_LIST
    else:
        package_list = DEBIAN_PACKAGE_LIST

    for p in package_list:
        p = host.package(p)
        assert p.is_installed


@pytest.mark.parametrize(
    "path",
    [
        ("/usr/local/pyenv"),
        ("/usr/local/pyenv/plugins/pyenv-virtualenv"),
    ],
)
def test_default_directories(host, path):
    d = host.file(path)
    assert d.is_directory
    assert d.user == "root"
    assert d.group == "root"
    assert d.mode == 0o755


def test_default_pyenv_versions(host):
    cmd = f"{PYENV_COMMAND_PREFIX} pyenv versions"
    result = host.run(cmd)

    if host.file("/usr/bin/python").is_file:
        assert result.exit_status == 0
        assert "* system" in result.stdout
    else:
        assert result.exit_status == 1
        assert "Warning: no Python detected on the system" in result.stderr


def test_default_pyenv_install(host):
    cmd = f"{PYENV_COMMAND_PREFIX} pyenv install 3.8.1"
    result = host.run(cmd)

    assert result.exit_status == 0


def test_default_pyenv_virtualenv(host):
    cmd = f"{PYENV_COMMAND_PREFIX} pyenv virtualenv 3.8.1 pytestvenv"
    result = host.run(cmd)

    assert result.exit_status == 0
