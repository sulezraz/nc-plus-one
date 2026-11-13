# ── Project configuration ────────────────────────────────────────
PROJECT_NAME = REST-API-deployment
REGION = eu-west-2
PYTHON_INTERPRETER = python
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip


# ── Create the virtual environment and install dependencies ───────
create-environment:
	@echo ">>> About to create environment: $(PROJECT_NAME)..."
	@echo ">>> check python3 version"
	( \
		$(PYTHON_INTERPRETER) --version; \
	)
	@echo ">>> Setting up venv."
	( \
		$(PYTHON_INTERPRETER) -m venv .venv; \
	)

# Activate the virtual environment for Python commands.
ACTIVATE_ENV := source .venv/bin/activate

define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

requirements: create-environment
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)


# ── Create development and test environment files (overwrites existing files) ──
create-dev-env:
	@echo ">>> Creating .env.development for the nc_plus_one database..."
	echo "PGDATABASE=nc_plus_one" > .env.development

create-test-env:
	@echo ">>> Creating .env.test for the test nc_plus_one database..."
	echo "PGDATABASE=nc_plus_one_test" > .env.test

create-envs: create-dev-env create-test-env



# ── Install development tools: Bandit, Black and coverage ─────────
bandit:
	$(call execute_in_env, $(PIP) install bandit)

black:
	$(call execute_in_env, $(PIP) install black)

coverage:
	$(call execute_in_env, $(PIP) install pytest-cov)

dev-setup: bandit black coverage


# ── Run security scanning and code formatting ────────────────────
security-test:
	$(call execute_in_env, bandit -lll */*.py *c/*/*.py)

run-black:
	$(call execute_in_env, black .)

run-checks: security-test run-black


# Create and seed database
create-db: 
	$(call execute_in_env, createdb nc_plus_one)
	$(call execute_in_env, $(PYTHON_INTERPRETER) -m reset_and_seed_database)

# ── Run tests and check code coverage (currently disabled) ─────────
# unit-test:
#	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v)

# check-coverage:
#	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest --cov=src tests/)

# run-tests: unit-test check-coverage

