#! /usr/bin/env python3
from argparse import ArgumentParser
from modules.inv import Loader
from modules.inv import Inventory


if __name__ == '__main__':

    args = ArgumentParser(description='Inventory Sample loader')
    args.add_argument('-s', '--script', type=str, required=True, help='path to the script to load')
    args = args.parse_args()

    inventory = Inventory()
    loader = Loader(inventory)
    rejections = loader.load(args.script)

    print("\n-------------------- Inventory loaded -----------------")
    print(f"Inventory loaded {len(inventory.query())} cars successfully. {len(rejections)} rejections")

    print("\n----------------- Query for BMW cars sorted by year -----------------")
    for car in inventory.query(make="BMW", sort_by="year"):
        print(str(car))

    print("\n----------------- Query for 2022 BMW X5 cars  -----------------")
    for car in inventory.query(make="BMW", year=2022, model="X5"):
        print(str(car))
