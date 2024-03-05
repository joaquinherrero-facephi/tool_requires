import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain
from conan.tools.files import copy

class ToolRecipe(ConanFile):
    name = "tool"
    version = "1.2.3"
    description = ""
    author = "Joaquin Herrero Herrero <joaquinherrero@facephi.com>"
    url = "None"
    topics = ("tool")
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    package_type = "application"

    def configure(self):
        # If we compile any missing dep it will hang forever.
        self.options["fmt"].shared = True

        # Instead if we set option header_only=True, it will work just fine
        # self.options["fmt"].header_only = True

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def requirements(self):
        self.requires("fmt/8.1.1", transitive_headers=False, transitive_libs=False, run=False, visible=False)
    
    def build(self):
        build_type_str = str(self.settings.build_type).lower()
        self.run(f"cmake --preset conan-{build_type_str}")
        self.run(f"cmake --build --preset conan-{build_type_str}")

    def package(self):
        package_bin_dir = os.path.join(self.package_folder, "bin")
        copy(self, "tool", self.build_folder, package_bin_dir, keep_path=False)

    def package_id(self):
        del self.info.requires["fmt"]

    def package_info(self):
        package_bin_dir = os.path.join(self.package_folder, "bin")
        self.buildenv_info.prepend_path("PATH", package_bin_dir)
    