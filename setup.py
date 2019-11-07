from setuptools import setup

setup(
	name='JSONMerger',
  version='1.0.0',
  description='Merge JSON .',
  authors_email=['tonyji146@gmail.com'],
  entry_points={
    'console_scripts': [
      'json_merger = merger.:json_merger'
    ],
  })