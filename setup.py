from setuptools import setup

import l10n


setup(
    name='tower',
    version=l10n.__version__,
    description='Pull strings from a variety of sources, collapse whitespace, '
                'support context (msgctxt), and merging .pot files.',
    long_description=open('README.rst').read(),
    author='Wil Clouser',
    author_email='wclouser@mozilla.com',
    url='http://github.com/clouserw/tower',
    license='BSD',
    packages=['l10n'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        # I don't know what exactly this means, but why not?
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)