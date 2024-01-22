.DEFAULT_GOAL := all
SHELL         :=  bash

ifeq ($(shell uname -s), Darwin)
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage
    MYPY          := mypy
    PYDOC         := pydoc3
    PYLINT        := pylint
    PYTHON        := python3
else ifeq ($(shell uname -p), x86_64)
    BLACK         := black-3.11
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage-3.11
    MYPY          := mypy-3.11
    PYDOC         := pydoc3.10
    PYLINT        := pylint-3.11
    PYTHON        := python3.11
else
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage
    MYPY          := mypy
    PYDOC         := pydoc
    PYLINT        := pylint
    PYTHON        := python
endif

# run docker
docker:
	docker run --rm -i -t -v $(PWD):/usr/python -w /usr/python gpdowning/python

# get git config
config:
	git config -l

# get git log
Grades.log.txt:
	git log > Grades.log.txt

# get git status
status:
	make --no-print-directory clean
	@echo
	git branch
	git remote -v
	git status

# download files from the Grades code repo
pull:
	make --no-print-directory clean
	@echo
	git pull
	git status

# upload files to the Grades code repo
push:
	make --no-print-directory clean
	@echo
	git add .gitignore
	git add .gitlab-ci.yml
	git add Grades.ctd.txt
	-git add Grades.html
	-git add Grades.log.txt
	git add Grades.py
	git add Makefile
	git add README.md
	git add run_Grades.py
	git add test_Grades.py
	git commit -m "another commit"
	git push
	git status

all:

# execute test harness with coverage
test:
	$(MYPY)   Grades.py
	$(MYPY)   test_Grades.py
	$(PYLINT) Grades.py
	$(PYLINT) test_Grades.py
	$(COVERAGE) run --branch test_Grades.py
	$(COVERAGE) report -m

# clone the Grades test repo
../cs373-grades-tests:
	git clone https://gitlab.com/gpdowning/cs373-grades-tests.git ../cs373-grades-tests

# generate a random input file
ctd-generate:
	$(CHECKTESTDATA) -g Grades.ctd.txt >> Grades.gen.txt

# execute the run harness against your test files in the Grades test repo and diff with the expected output
run: ../cs373-grades-tests
	$(MYPY)   Grades.py
	$(MYPY)   run_Grades.py
	$(PYLINT) Grades.py
	$(PYLINT) run_Grades.py
	$(CHECKTESTDATA) Grades.ctd.txt ../cs373-grades-tests/gpdowning-Grades.in.txt    # change gpdowning to your GitLab-ID
	./run_Grades.py < ../cs373-grades-tests/gpdowning-Grades.in.txt > Grades.tmp.txt # change gpdowning to your GitLab-ID
	diff Grades.tmp.txt ../cs373-grades-tests/gpdowning-Grades.out.txt               # change gpdowning to your GitLab-ID

# execute the run harness against all of the test files in the Grades test repo and diff with the expected output
run-all: ../cs373-grades-tests
	$(MYPY)   Grades.py
	$(MYPY)   run_Grades.py
	$(PYLINT) Grades.py
	$(PYLINT) run_Grades.py
	-@for v in `ls ../cs373-grades-tests/*.in.txt`;             \
    do                                                                 \
        echo $(CHECKTESTDATA) Grades.ctd.txt $${v};             \
             $(CHECKTESTDATA) Grades.ctd.txt $${v};             \
        echo ./run_Grades.py \< $${v} \> Grades.tmp.txt; \
             ./run_Grades.py  < $${v}  > Grades.tmp.txt; \
        echo diff Grades.tmp.txt $${v/.in/.out};                \
             diff Grades.tmp.txt $${v/.in/.out};                \
    done

# auto format the code
format:
	$(BLACK) Grades.py
	$(BLACK) run_Grades.py
	$(BLACK) test_Grades.py

# create html file
Grades.html: Grades.py
	-$(PYDOC) -w Grades

# check files, check their existence with make check
C_FILES :=          \
    .gitignore      \
    .gitlab-ci.yml  \
    Grades.html    \
    Grades.log.txt

# check the existence of check files
check: $(C_FILES)

# remove temporary files
clean:
	rm -f  .coverage
	rm -f  *.gen.txt
	rm -f  *.tmp.txt
	rm -rf __pycache__
	rm -rf .mypy_cache

# remove temporary files and generated files
scrub:
	make --no-print-directory clean
	rm -f Grades.html
	rm -f Grades.log.txt

# output versions of all tools
versions:
	uname -p

	@echo
	uname -s

	@echo
	which $(BLACK)
	@echo
	$(BLACK) --version | head -n 1

	@echo
	which $(CHECKTESTDATA)
	@echo
	$(CHECKTESTDATA) --version | head -n 1

	@echo
	which $(COVERAGE)
	@echo
	$(COVERAGE) --version | head -n 1

	@echo
	which git
	@echo
	git --version

	@echo
	which make
	@echo
	make --version | head -n 1

	@echo
	which $(MYPY)
	@echo
	$(MYPY) --version

	@echo
	which pip
	@echo
	pip --version

	@echo
	which $(PYDOC)

	@echo
	which $(PYLINT)
	@echo
	$(PYLINT) --version | head -n 1

	@echo
	which $(PYTHON)
	@echo
	$(PYTHON) --version

	@echo
	which vim
	@echo
	vim --version | head -n 1
