from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirments.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirment_file:
        requirment_list = requirment_file.readlines()
    requirment_list = [requirment_name.replace("\n", "") for requirment_name in requirment_list]
    
    if HYPHEN_E_DOT in requirment_list:
        requirment_list.remove(HYPHEN_E_DOT)
    return requirment_list    



setup(
    name = "sensor",
    version = "0.0.1",
    author= "Ankur Singh",
    author_email= "ankursingh037@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements(),
)