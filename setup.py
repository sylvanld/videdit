import setuptools

setuptools.setup(
    name="videdit",
    description="Set of commands used to edit video files",
    version="0.0.1",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "videdit=videdit.__main__:main"
        ]
    }
)
