# Car Inventory Example
- code source: https://github.com/PoohCook/car_inventory


# This project was broken into the following steps
- Create Manufacturer
- Create Car with manufacturer
- Add Trademark inclusion
- Create Inventory Repository object
- Add Query tools to Inventory object
- Implement Inventory Loader
- Add example run module


# to run artifacts
- make test
    This command will run the tests for all modules

- make lint
    This command will run python lint checking for all modules

- make run
    This command will run the sample program

- make clean
    This command cleans up any temp caches

- make package
    This command compresses the current project into a gzipped tar file
    this tar file can be uncompressed with
    ```
        tar -xvf ./car_inventory.tar.gz
        unzip ./car_inventory.zip
    ```


# Notes

- Vehicle Id Number:  https://en.wikipedia.org/wiki/Vehicle_identification_number
    17 characters, and only uses capital letters (excluding I, O and Q) and digits (0-9)
