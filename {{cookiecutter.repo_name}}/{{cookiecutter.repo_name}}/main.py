#!/usr/bin/env python
# -*- coding: utf-8 -*-

from {{cookiecutter.repo_name}} import {{cookiecutter.app_class_name}}

def main():
    res = {{cookiecutter.app_class_name}}().run()
    print(res)

if __name__ == '__main__':
    main()
