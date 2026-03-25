from setuptools import setup, find_packages
setup(
    name="evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos",
    version="1.0.0",
    description="Evolucion del Salario Minimo y Salario Medio en Latinoamerica 2000-2024 Base de Datos por País. DOI:",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/evolucion-salario-minimo-y-medio-latinoamerica-2000-2024-base-de-datos",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)