KATTIS_CLI_PATH := ../kattis-cli
KATTIS_PROBLEM := cosmicpathoptimization
FILES := ../cosmicpathoptimization/main.py


all: check_types check_format local_test unit_test autopep submit clean

check_types:
ifeq ($(shell which mypy), )
		@echo "mypy not found. Installing mypy..."
		pip install mypy
endif
	@mypy --strict --disallow-untyped-defs main.py
	@echo "Type checking passed! \n"

check_format:
	flake8 main.py
	@echo "Format checking passed! \n"

unit_test:
	@pytest test_main.py
	@echo "Unit tests passed! \n"

autopep:
ifeq ($(shell which autopep8), )
		@echo "autopep8 not found. Installing autopep8..."
		pip install autopep8
endif
	@echo "Running autopep8..."
	autopep8 main.py
	@echo "Auto formatting completed! \n"

local_test:
	@cat 1.in | python3 main.py > main1.txt
	diff main1.txt 1.ans
	@echo "Local Tests Passed!"

submit:
	@echo "Submitting solution to Kattis..."
	cd $(KATTIS_CLI_PATH) && \
	python3 submit.py -p $(KATTIS_PROBLEM) $(FILES)
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
