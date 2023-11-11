from setuptools import find_packages,setup
from typing import List

unwanted = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if unwanted in requirements:
            requirements.remove(unwanted)
            
    return requirements


# Giving the description about the project
setup(
name = 'MLOps integration',
version = '0.0.1',
author = 'abhisek',
author_email = 'abhisekmaharana9861@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)