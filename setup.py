from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='python_gyg',
      version='0.1',
      description='Python library for GetYourGuide API',
      url='http://github.com//fukac99/python_gyg.git',
      long_description=readme(),
      keywords=['getyourguide', 'travel', 'api', 'tours'],
      classifiers=[
	'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
],
      author='Lukas Toma',
      install_requires=["requests", "datetime"],
      author_email='toma.lukas@gmail.com',
      license='MIT',
      packages=['python_gyg'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose', "datetime"])
