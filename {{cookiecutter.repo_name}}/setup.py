from setuptools import setup, find_packages
setup(
    name = "{{cookiecutter.repo_name}}",
    version = "{{cookiecutter.version}}",
    packages = find_packages(),
    scripts = ['{{cookiecutter.repo_name}}/main.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires = ['docutils>=0.3'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'),
        # And include any *.msg files found in the {{cookiecutter.repo_name}} package, too:
        '{{cookiecutter.repo_name}}': ['*.msg'],
    },

    # metadata for upload to PyPi
    author = "{{cookiecutter.full_name}}",
    author_email = "{{cookiecutter.email}}",
    description = "{{cookiecutter.short_description}}",
    license = "{{cookiecutter.license}}",
    keywords = "{{cookiecutter.repo_name}} {{cookiecutter.app_class_name}} {{cookiecutter.app_title}}",
    url = "https://www.github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}",

)
