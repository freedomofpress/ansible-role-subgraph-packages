DEFAULT_GOAL: help
SHELL := /bin/bash
PWD := $(shell pwd)

.PHONY: test-packages
test-packages: ## Configures container with SGOS packages.
	molecule test -s default

.PHONY: test-upgrade
test-upgrade: ## Configures container with full upgrade to SGOS repos.
	molecule test -s all-packages

.PHONY: test-kernel
test-kernel: ## Configures libvirt VM with SGOS hardened kernel.
	molecule test -s grsec-kernel

.PHONY: test
test: test-packages test-upgrade test-kernel ## Runs all tests from a clean slate.

.PHONY: ci
ci: test-packages test-upgrade # Runs all container tests (no VMs).

# Explanation of the below shell command should it ever break.
# 1. Set the field separator to ": ##" and any make targets that might appear between : and ##
# 2. Use sed-like syntax to remove the make targets
# 3. Format the split fields into $$1) the target name (in blue) and $$2) the target descrption
# 4. Pass this file as an arg to awk
# 5. Sort it alphabetically
# 6. Format columns with colon as delimiter.
.PHONY: help
help: ## Print this message and exit.
	@printf "Subcommands:\n\n"
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%s\033[0m : %s\n", $$1, $$2}' $(MAKEFILE_LIST) \
		| sort \
		| column -s ':' -t
