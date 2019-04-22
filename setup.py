from setuptools import setup, find_packages

setup(
    name='pyAIY',
    version='1.2',
    description='AIY Python API',
    author='AIY Team',
    author_email='support-aiyprojects@google.com',
    url="https://aiyprojects.withgoogle.com/",
    project_urls={
        'GitHub: issues': 'https://github.com/google/aiyprojects-raspbian/issues',
        'GitHub: repo': 'https://github.com/google/aiyprojects-raspbian',
    },
    license='Apache 2',
    packages=find_packages(),
    install_requires=[
        'RPi.GPIO',
    ],
    python_requires='>=3.5.3',
)
