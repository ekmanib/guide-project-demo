setup:
	make install-tests
	make install-jupyter
	make setup-pre-commit

# black: https://github.com/psf/black
# flake8: https://github.com/pycqa/flake8
# isort: https://github.com/PyCQA/isort
# nbstripout: https://github.com/kynan/nbstripout
# pydocstyle: https://github.com/PyCQA/pydocstyle
# pre-commit-hooks: https://github.com/pre-commit/pre-commit-hooks
# interrogate: https://interrogate.readthedocs.io/en/latest/index.html?highlight=pre-commit

setup-pre-commit:
	poetry add --group dev flake8 isort nbstripout pydocstyle pre-commit-hooks interrogate sourcery mypy pylint bandit black

install-pre-commit:
	poetry run pre-commit install

install-jupyter:
	poetry add ipykernel --group dev
	poetry add --group dev jupyterlab
	poetry add jupyterlab_execute_time --group dev

install-tests:
	poetry add hydra-core
	poetry add pytest allure-pytest --group dev
	poetry add pytest-cov --group dev
	poetry add pytest-clarity pytest-sugar --group dev

# https://timvink.github.io/mkdocs-git-authors-plugin/index.html
install-docs:
	poetry add --group docs mkdocs mkdocs-material
	poetry add --group docs mkdocs-git-revision-date-localized-plugin
	poetry add --group docs mkdocs-minify-plugin
	poetry add --group docs mkdocs-redirects
	poetry add --group docs mkdocs-awesome-pages-plugin
	poetry add --group docs mkdocs-git-authors-plugin
	poetry add --group docs mkdocstrings\[python\]
	poetry add --group docs mkdocs-bibtex
	poetry add --group docs mkdocs-macros-plugin
	poetry add --group docs mkdocs-jupyter
	poetry add --group docs mkdocs-callouts
	poetry add --group docs mkdocs-glightbox

test:
	poetry run pytest -vs --clean-alluredir --alluredir tmp/allure_results --cov=src --no-cov-on-fail

report:
	poetry run allure serve tmp/allure_results
