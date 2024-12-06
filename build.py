from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("python.flake8")
# Comment out or remove these plugins to skip tests and coverage
# use_plugin("python.unittest")
# use_plugin("python.coverage")

name = "my_cloud_devops_consulting"
version = "0.1.0"
summary = "A consulting website built with Flask"
license = "MIT"
default_task = "publish"

@init
def initialize(project):
    # Specify Python version
    project.build_depends_on("wheel")
    project.depends_on("flask")  # Keep your valid dependencies here
    project.set_property("distutils_classifiers", [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"
    ])
    project.set_property("distutils_commands", ["sdist", "bdist_wheel"])
    project.set_property("distutils_upload_repository", "https://upload.pypi.org/legacy/")
    project.set_property("distutils_upload_sign", True)
    project.set_property("distutils_upload_sign_identity", None)  # Set to your key identity
    project.set_property("flake8_break_build", True)
