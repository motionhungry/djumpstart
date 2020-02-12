import os
import shutil
import stat
from random import choice

import click


ROOT_DIR = os.path.dirname(__file__)
PROJECT_TEMPLATE_DIR = os.path.join(ROOT_DIR, 'project_template')
APP_TEMPLATE_DIR = os.path.join(ROOT_DIR, 'app_template')

RANDOM_CHOICES = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*-_=+'


@click.group()
def main():
    pass


@main.command()
@click.argument('project_name')
@click.option('--template', default=PROJECT_TEMPLATE_DIR)
@click.option('--destination', default=os.getcwd())
def startproject(project_name, template, destination):
    """
    Create a new Django project
    """
    destination = os.path.join(destination, project_name)
    template_context = {
        'project_name': project_name,
        'secret_key': ''.join([choice(RANDOM_CHOICES) for i in range(64)]),
        'postgres_user': ''.join([choice(RANDOM_CHOICES) for i in range(16)]),
        'postgres_password': ''.join([choice(RANDOM_CHOICES) for i in range(32)]),
        'celery_flower_user': ''.join([choice(RANDOM_CHOICES) for i in range(16)]),
        'celery_flower_password': ''.join([choice(RANDOM_CHOICES) for i in range(32)]),
    }
    build_template(template, destination, template_context)
    click.echo('{} project created.'.format(project_name))


@main.command()
@click.argument('app_name')
@click.option('--template', default=APP_TEMPLATE_DIR)
@click.option('--destination', default=os.getcwd())
def startapp(app_name, template, destination):
    """
    Create an app in an existing Django project
    """
    destination = os.path.join(destination, app_name)
    template_context = {
        'app_name': app_name,
        'camel_case_app_name': app_name.replace('_', ' ').title().replace(' ', ''),
    }
    build_template(template, destination, template_context)
    click.echo('{} app created.'.format(app_name))


def build_template(src_dir, dest_dir, template_context):
    """
    Copies template to destination directory and applies template context
    """
    for path, dirs, files in os.walk(src_dir):
        relative_path = path[len(src_dir):].lstrip(os.sep)
        for placeholder, value in template_context.items():
            relative_path = relative_path.replace(placeholder, value)
        os.mkdir(os.path.join(dest_dir, relative_path))
        for filename in files:
            src_path = os.path.join(path, filename)
            for placeholder, value in template_context.items():
                filename = filename.replace(placeholder, value)
            dest_path = os.path.join(dest_dir, relative_path, filename)
            build_template_file(src_path, dest_path, template_context)


def build_template_file(src_path, dest_path, template_context):
    """
    Copies template file to destination directory and applies template context
    """
    # Read the original file and apply the template context
    src_file = open(src_path, 'r')
    data = src_file.read()
    src_file.close()
    for placeholder, value in template_context.items():
        data = data.replace('{{ %s }}' % placeholder, value)

    # Write the new file
    dest_file = open(dest_path, 'w')
    dest_file.write(data)
    dest_file.close()

    # Copy file permissions
    shutil.copymode(src_path, dest_path)

    # Make new file writeable
    if os.access(dest_path, os.W_OK):
        st = os.stat(dest_path)
        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
        os.chmod(dest_path, new_permissions)


main.add_command(startproject)
main.add_command(startapp)


if __name__ == '__main__':
    main()
