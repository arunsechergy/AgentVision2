import setuptools

with open('README.md', 'r', encoding='utf8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    required = fh.read().splitlines()

setuptools.setup(
    name="arunsechergy",
    version="2.2",
    author="Arun Kumar RN",
    author_email="arun.rvbe@gmail.com",
    description="AgentVision 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arunsechergy/AgentVision2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
    include_package_data=True,
)
