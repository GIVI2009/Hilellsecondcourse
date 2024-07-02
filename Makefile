.PHONY: run
run:
	echo '😀'
	echo 'UA'
	@echo 'GIIIITTTT'
	python main.py
	python gg.py

.PHONY: ins
ins:
	pip install poetry
	poetry config --local virtualenvs.in-project true
	poetry init -n
	poetry install
	.\.venv\Scripts\activate
	poetry add fastapi