from distutils.core import setup

setup(
    name='waaave-gravatar',
    version='0.5.1',
    description='Gravatar Support in a Django Reusable Application',
    author='Valerian Saliou',
    author_email='valerian@valeriansaliou.name',
    url='https://github.com/valeriansaliou/waaave-gravatar',
    packages=[
        'gravatar',
        'gravatar.templatetags',
    ],
    classifiers=[
        'Development Status :: 2 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
