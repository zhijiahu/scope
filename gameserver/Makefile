
CXX = g++
CXXFLAGS += -std=c++11

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
project_path := $(dir $(mkfile_path))

build: ensure-bin server-dynamic server-static

server-dynamic: server.o
	$(CXX) $^ -o $(project_path)bin/$@

server-static: server.o
	$(CXX) $^ -o $(project_path)bin/$@ -static

ensure-bin:
	-mkdir $(project_path)bin

clean:
	-rm -r $(project_path)bin
	-rm *.o
