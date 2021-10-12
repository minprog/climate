bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)

# get all subdirectories
wild := $(wildcard */)

# remove trailing slash
dirs := $(subst /,,$(wild))

# generate zipfiles for each subdirectory
all: message $(addsuffix .zip,$(dirs))

# print current dir before zipping, using ansi bold
message:
	@echo '$(bold)$(shell pwd)$(sgr0)'

# ensure that $$ are expanded to allow the subdir name in $* to be used in source pattern
.SECONDEXPANSION:

# each zip can be generated from a subdirectory of the same name (stem)
%.zip: $$(wildcard $$*/*)
	zip -9 -r -q $@ $^
