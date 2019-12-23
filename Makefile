# Makefile

## Configuration

BUILD_TIME := $(shell date +%FT%T%z)
PROJECT    := $(shell basename $(PWD))


## Install dependencies
.PHONY: install
install:
	python3 -m pip install -r --user requirements.txt

## Setup developpement environment
.PHONY: dev
dev:
	cd app && ln -sf config_dev.py config.py

## Setup production environment
.PHONY: prod
prod:
	cd app && ln -sf config_prod.py config.py
