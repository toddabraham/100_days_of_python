from setuptools import find_packages, setup
with open('README.md', 'r') as f:
 long_description = f.read()
setup(
 name='100_days_python',
 version='0.1.0',
 author='Todd Abraham',
 author_email='todd.apis@gmail.com',
 description='Various projects built during 100 Days of Python Bootcamp',
 long_description=long_description,
 long_description_content_type='text/markdown',
 url='https://github.com/toddabraham/100_days_of_python.git',
 packages=find_packages('src')
)