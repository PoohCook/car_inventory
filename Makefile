
MAKE = make
COMMON_DIR = ../
.PHONY: test lint


test:
	export PATH=$(shell pwd):$$PATH; ./RunAllUnitTests.py -f

lint:
	pycodestyle modules test --config=.pycodestyle.cfg
	pygount ./modules | awk '$$1 >= 100'
