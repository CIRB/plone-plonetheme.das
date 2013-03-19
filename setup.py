from setuptools import setup, find_packages

version = '1.2.4.dev0'

setup(name='plonetheme.das',
      version=version,
      description="An Installable theme for Plone 4",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Fabrice Monaco',
      author_email='fmonaco@cirb.irisnet.be',
      url='',
      license='Creative Commons Attribution 3.0 Unported',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )

