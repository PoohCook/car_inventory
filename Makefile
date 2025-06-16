
MAKE = make
COMMON_DIR = ../
.PHONY: test lint

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

test:
	export PATH=$(shell pwd):$$PATH; ./RunAllUnitTests.py -f

lint:
	pycodestyle modules test --config=.pycodestyle.cfg
	pygount ./modules | awk '$$1 >= 100'
