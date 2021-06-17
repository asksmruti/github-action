from setuptools import setup, find_packages

setup(name='github_action_demo',
      version='0.1',
      description='Github Action Demo',
      url='https://github.com/asksmruti/github-action.git',
      author='Smruti',
      license='MIT',
      packages=find_packages(include=['gh_action_demo']),
      install_requires=[
            'geocoder==1.38.1',
            'Flask==1.1.2',
            'uvicorn==0.14.0'
      ],
      setup_requires=['pytest-runner', 'flake8'],
      tests_require=['pytest']
      )
