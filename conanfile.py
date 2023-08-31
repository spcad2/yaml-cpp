import os
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.scm import Git
from conan.tools.files import load, update_conandata

build_requires = "cmake/3.19.2"

class YamlCppConan(ConanFile):
    name = "yaml-cpp"
    version = "0.8.0"
    description = "A YAML parser and emitter in C++"
    homepage = "https://github.com/jbeder/yaml-cpp"
    url = "https://github.com/spcad2/yaml-cpp.git"
    license = "MIT"
    generators = "cmake_find_package"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"    

    def build(self):
        # build() will have access to the sources, obtained with the clone in source()
        cmake = CMake(self)
