from setuptools import find_packages, setup
from typing import List

HYPEN_E = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    req
    '''
    requirments = []
    with open (file_path) as file_object
        requirments = file_object.readlines()
        requirments= [req.replce("\n", "") for req in requirments]
        if HYPEN_E in requirments:
            requirments.remove(HYPEN_E)
    return requirments


setup(
    name = 'ML-Project',
    version='0.0.1',
    author='Guru Alampalli',
    author_email='Guru.Alampalli@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)