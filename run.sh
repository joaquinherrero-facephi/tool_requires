conan remove "tool*" -c  
conan export tool
conan install -pr:h profile_host -pr:b profile_build tool -b missing