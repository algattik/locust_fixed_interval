import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='locust_fixed_interval',
    version='0.1',
    author="Alexandre Gattiker",
    author_email="algattik@microsoft.com",
    description="Fixed interval taskset utility package for Locust",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/algattik/locust_fixed_interval",
    packages=setuptools.find_packages(),
    install_requires=[
        'locust',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
