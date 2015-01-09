# -*- coding: utf-8 -*-
__revision__ = "$Id: setup.py 16731 2014-06-02 15:42:19Z gbaty $"


from setuptools import setup

name = 'codeeditor'
version = '0.1'
description = 'Source Code Editors for OpenAleaLab'
long_description = description
authors = 'VP'
authors_email = 'vp'
url = 'url'


setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=authors,
    author_email=authors_email,
    url=url,
    license=license,
    keywords='',

    # package installation
    packages=['spydereditor', 'pyqodeeditor', 'quteparteditor', 'enkieditor'],
    package_dir={
        'spydereditor': 'spydereditor',
        'pyqode': 'pyqodeeditor',
        'qutepart': 'quteparteditor',
        'enki': 'enkieditor',
    },

    zip_safe=False,
    include_package_data=True,

    # Declare src and wralea as entry_points (extensions) of your package
    entry_points={

        'oalab.applet': [
            'PyQodeEditor = pyqodeeditor.plugin:PyQodeEditorPlugin',
        ],

    },
)
