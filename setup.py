from setuptools import setup

setup(name = 'artificial-bee-colony',
version = "1.0.0.dev1",
description = 'Artificial bee colony for parameters tuning based on fitness scores',
url = 'https://github.com/hgromer/Artificial-Bee-Colony',
author = 'Hernan Gelaf-Romer',
author_email = 'Hernan_Gelafromer@student.uml.edu',
license = 'MIT',
packages = ['abc'],
install_requires = ["random", "numpy"],
zip_safe = False)