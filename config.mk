export GNFINDER_VERSION = v0.14.1
export GNVERIFIER_VERSION = v0.3.1

export UNAME := $(shell uname)

PLATFORM := unsupported
ifeq ($(OS),Windows_NT)
	PLATFORM := unsupported
else
	UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        PLATFORM := linux
    endif
    ifeq ($(UNAME_S),Darwin)
        PLATFORM := mac
    endif
endif