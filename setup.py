from setuptools import setup, find_packages

setup(
    name='speaker_verification',
    version='0.1.0',
    packages=find_packages(include=['speaker_verification', 'speaker_verification.*'])
)
