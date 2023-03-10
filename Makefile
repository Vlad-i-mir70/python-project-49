install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain_calc:
	poetry run brain-calc
brain-progression:
	poetry run brain_progression
brain-gcd:
	poetry run brain_gcd
brain-prime:
	poetry run brain_prime
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games
