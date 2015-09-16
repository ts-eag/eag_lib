from os import path
from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run, cd
import random

REPO_URL = 'https://github.com/ts-eag/eag_lib.git'


def deploy():
    # site_folder = '/home/{}/_git/{}'.format(env.user, env.host)
    folder_name = 'eag_lib'
    site_folder = '/home/{}/_git/{}'.format(env.user, folder_name)
    print('site_folder....', site_folder)
    print(env.user)
    assert site_folder, 'root'
    source_folder = site_folder + '/source'
    python_url = 'https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz'
    pip_url = 'https://bootstrap.pypa.io/get-pip.py'
    _install_development_tools()
    _install_python(python_url)
    _install_pip(site_folder, pip_url)
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _make_virtualenv(source_folder)
    # _update_settings(source_folder, env.host)
    # _update_virtualenv(source_folder)
    # _update_static_files(source_folder)
    # _update_database(source_folder)


def _install_development_tools():
    run('yum -y install gcc')
    run('yum -y install openssl-devel bzip2-devel sqlite-devel zlib-devel')
    run('yum -y install git')


def _install_python(python_url):
    current_python = run('python --version')
    if not '2.7' in current_python:
        with cd('/tmp'):
            run('wget {}'.format(python_url))
            fname = path.split(python_url)[-1]
            run('tar Jxvf {}'.format(fname))
            fname = fname.replace('.tar.xz', '')
            with cd(fname):
                run('./configure')
                run('make && make altinstall')
            run('ln -s /usr/local/bin/python2.7 /usr/local/bin/python')
        settings_bash_profile = '~/.bash_profile'
        append(settings_bash_profile, '\nPATH=/usr/local/bin:$PATH\nexport PATH')
        run('source ~/.bash_profile')


def _install_pip(site_folder, pip_url):
    current_pip = run('pip --version')
    if not '2.7' in current_pip:
        with cd('/tmp'):
            run('wget --no-check-certificate {}'.format(pip_url))
            fname = path.split(pip_url)[-1]
            run('python2.7 {}'.format(fname))
    run('pip2.7 install virtualenv')
    run('pip2.7 install virtualenvwrapper')
    settings_bashrc = '~/.bashrc'
    print('site_folder....', path.join(site_folder, 'virtualenv'))
    print('site_folder....', site_folder)
    append(settings_bashrc, '\nexport WORKON_HOME={}'.format(
        path.join(site_folder, 'virtualenv')))
    append(settings_bashrc, '\nsource /usr/local/bin/virtualenvwrapper.sh')
    run('source ~/.bashrc')

# def _make_virtualenv(folder_name):
#     run('mkvirtualenv {}'.format(folder_name))


def _create_directory_structure_if_necessary(site_folder):
    # for subfolder in ('database', 'static', 'virtualenv', 'source'):
    for subfolder in ('database', 'static', 'virtualenv'):
        run('mkdir -p {site_folder}/{subfolder}'.format(site_folder=site_folder,
                                                        subfolder=subfolder))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        with cd(source_folder):
            run('git fetch')
    else:
        run('git clone {} {}'.format(REPO_URL, source_folder))
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run('git reset --hard {}'.format(current_commit))


def _make_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv/python2'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python2 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (
        virtualenv_folder, source_folder
                                                      )
    )

















# def _update_settings(source_folder, site_name):
#     settings_path = source_folder + '/superlists/settings.py'
#     sed(settings_path, 'DEBUG = True', 'DEBUG = False')
#     sed(settings_path,
#         'ALLOWED_HOSTS =.+$',
#         'ALLOWED_HOSTS = ["{}"]'.format(site_name))
#     secret_key_file = source_folder + '/superlists/secret_key.py'
#     if not exists(secret_key_file):
#         chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
#         key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
#         append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
#     append(settings_path, '\nfrom .secret_key import SECRET_KEY')
#
#
# def _update_virtualenv(source_folder):
#     virtualenv_folder = '{0}'.format(path.join(source_folder, '..', 'virtualenv'))
#     if not exists(path.join(virtualenv_folder, 'bin', 'pip')):
#         run('virtualenv {}'.format(virtualenv_folder))
#     run('%s/bin/pip install -r %s/requirements.txt' % (
#         virtualenv_folder, source_folder))
#
#
# def _update_static_files(source_folder):
#     with cd(source_folder):
#         run('{} manage.py collectstatic --noinput'.format(
#             path.join('..', 'virtualenv', 'bin', 'python2')))
#
#
# def _update_database(source_folder):
#     with cd(source_folder):
#         run('{} manage.py migrate --noinput'.format(
#             path.join('..', 'virtualenv', 'bin', 'python2')))