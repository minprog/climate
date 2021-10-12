# find all subdirectories named `dist`, run `make` there
all:
	@find . -name dist -type d -exec make -C {} \;
