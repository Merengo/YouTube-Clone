from setuptools import setup,find_packages

# with open("README", 'r') as f:
#     long_description = f.read()

setup(
   name='youtube',
   version='1.0',
   description='A useful module',
   license="MIT",
   long_description=long_description,
   author='Man Foo',
   author_email='marwamerengo@gmail.com',
   url="",
   packages=find_packages(),  #same as name
   install_requires=[], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)