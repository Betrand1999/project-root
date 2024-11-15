from setuptools import setup, find_packages

setup(
    name='my-cloud-devops-consulting',  # Use a unique project name
    version='0.1.1',  # Updated version
    author='Betrand Mutagha',
    author_email='mmutagha@gmail.com',
    description='This is my consulting website for Cloud & DevOps services.',
    long_description=open('README.md').read(),  # Make sure README.md exists
    long_description_content_type='text/markdown',
    url='https://github.com/Betrand1999/project-root',  # Replace with your GitHub project URL
    packages=find_packages(),  # Automatically find all packages in the current directory
    install_requires=[
        'Flask>=2.0',  # Add Flask as a dependency
        'pymongo',  # Example for MongoDB driver
        'werkzeug',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
