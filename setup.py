from setuptools import setup, find_packages
import os

version = '1.0'


tests_require = [
     'ftw.inflator',
     'ftw.testing',
     'Products.PloneTestCase',
     'plone.app.testing',
     'zope.configuration',
    ]

extras_require = {
    'tests': tests_require,
    }

setup(name='ftw.ech0039',
      version=version,
      description="Swiss e-government data exchange interface for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Thomas Buchberger',
      author_email='t.buchberger@4teamwork.ch',
      url='http://www.4teamwork.ch',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.api',
          'plone.uuid',
          'setuptools',
          'PyXB<=1.2.1',  # generated bindings do not work with 1.2.2
          'Products.CMFCore',
          'Products.ATContentTypes',
          'zope.interface',
          'zope.component'
      ],
      tests_require=tests_require,
      extras_require=extras_require,
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone

      [console_scripts]
      pyxbgen = ftw.ech0039.pyxbgen:main
      """,
      )
