from setuptools import setup, find_packages


setup(
    name='mudsling-furniture',
    license='MIT',
    author='Josh Benner',
    author_email='josh@bennerweb.com',

    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['mudsling'],

    entry_points={
        'mudsling.plugin': [
            'furniture = mudsling_furniture:FurniturePlugin'
        ]
    }
)
