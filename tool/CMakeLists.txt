cmake_minimum_required(VERSION 3.21)

project(tool CXX)

add_executable(${PROJECT_NAME})

find_package(fmt REQUIRED)

file(GLOB_RECURSE SOURCES "src/*.cpp")

target_sources(${PROJECT_NAME} PRIVATE ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE "include/")

target_link_libraries(${PROJECT_NAME}
	PRIVATE
		fmt::fmt-header-only
		$<$<CXX_COMPILER_ID:GNU>:stdc++fs>
        $<$<CXX_COMPILER_ID:Clang>:c++fs>)
