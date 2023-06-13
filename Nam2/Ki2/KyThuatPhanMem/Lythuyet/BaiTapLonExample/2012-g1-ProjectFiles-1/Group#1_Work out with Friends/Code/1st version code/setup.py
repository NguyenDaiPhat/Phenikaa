from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'waitress',
    'WebTest',
    'zope.sqlalchemy',
    ]

setup(name='wowf',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='wowf',
      install_requires=requires,
      entry_points={
          'paste.app_factory': ['main=wowf:main'],
          'console_scripts': [
              'wowf_adduser=wowf.scripts.adduser:main',
              'wowf_cleanup=wowf.scripts.cleanup:main',
              'wowf_indexer=wowf.scripts.indexer:main',
              'wowf_initializedb=wowf.scripts.initializedb:main',
              'wowf_sendinvite=wowf.scripts.sendinvite:main',
              ],
          },
      )