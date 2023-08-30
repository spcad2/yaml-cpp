import os
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.scm import Git
from conan.tools.files import load, update_conandata


class YamlCppConan(ConanFile):
    name = "yaml-cpp"
    version = "0.8.0"
    description = "A YAML parser and emitter in C++"
    homepage = "https://github.com/jbeder/yaml-cpp"
    url = "https://github.com/spcad2/yaml-cpp.git"
    license = "MIT"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"    

    def export(self):
        git = Git(self, self.recipe_folder)
        scm_url, scm_commit = git.get_url_and_commit()
        # we store the current url and commit in conandata.yml
        update_conandata(self, {"sources": {"commit": scm_commit, "url": scm_url}})

    def layout(self):
        cmake_layout(self, src_folder=".")

    def source(self):
        # we recover the saved url and commit from conandata.yml and use them to get sources
        git = Git(self)
        sources = self.conan_data["sources"]
        git.clone(url=sources["url"], target=".")
        git.checkout(commit=sources["commit"])

    def build(self):
        # build() will have access to the sources, obtained with the clone in source()
        cmake = CMake(self)
        cmake.definitions["CONAN_SETTINGS_ARCH"] = self.settings.arch
        cmake.definitions["CMAKE_BUILD_TYPE"] = self.settings.build_type
        cmake.definitions["CMAKE_CONFIGURATION_TYPES"] = self.settings.build_type
        cmake.definitions["CMAKE_SOURCE_FOLDER"] = self.source_folder        
        cmake.configure()
        cmake.build()