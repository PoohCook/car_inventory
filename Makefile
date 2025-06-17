
MAKE = make
COMMON_DIR = ../
.PHONY: test lint

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm *.tar.gz

test:
	export PATH=$(shell pwd):$$PATH; ./RunAllUnitTests.py -f

lint:
	pycodestyle modules test ./sample.py --config=.pycodestyle.cfg
	pygount ./modules | awk '$$1 >= 100'

run:
	./sample.py -s test/scripts/inv_sample.json

package: clean
	tar -czf ../car_inventory.tar.gz ./
	mv ../car_inventory.tar.gz ./car_inventory.tar.gz
