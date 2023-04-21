import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
        name="AutomaticHourglass", # Replace with your username
        version="1.0.0",
        author="unsal Gokdag",
        author_email="<authorname@templatepackage.com>",
        description="A robust JSON encoder that fixes errors by utilizing DFS algorithm.",
        long_description=long_description,
        url="https://github.com/AutomaticHourglass/dfsjson",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )