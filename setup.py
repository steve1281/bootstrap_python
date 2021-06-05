from setuptools import setup, find_packages

NAME = "bootstrap_python"
VERSION = "0.0.1"

REQUIRES = [
]

long_description = "Longer Markdown; sometimes we just read in the README.md file"

setup(
    name=NAME,
    extras_require=dict(test=['pytest']),
    version=VERSION,
    description="Description of the project",
    install_requires=REQUIRES,
    packages=find_packages('src'),
    package_dir={"": "src"},
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    use_scm_version = {
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "node-and-timestamp"
    },
    package_data={'': ['templates/*.*']},
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts":["bootstrap_python = bootstrap_python.__main__:main"]
    },
    long_description=long_description,
)
