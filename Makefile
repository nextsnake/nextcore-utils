build:
	python -m build

install:
	pip install .

install-editable:
	pip install -e . --config-settings editable_mode=compat

test:
	ruff .