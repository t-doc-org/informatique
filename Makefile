# Copyright 2024 Caroline Blank <caro@c-space.org>
# Copyright 2024 Remy Blank <remy@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

PYTHON ?= python
PYTHONPATH ?=

.PHONY: Makefile.local
-include Makefile.local

_COMMON_MK := $(shell PYTHONPATH="$(PYTHONPATH)" $(PYTHON) \
				-c 'from tdoc.common import makefile; print(makefile)')
ifneq ($(.SHELLSTATUS),0)
  $(error t-doc/common package not found)
endif
.PHONY: $(_COMMON_MK)
include $(_COMMON_MK)
