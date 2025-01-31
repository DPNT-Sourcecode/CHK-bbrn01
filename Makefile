run:
	python lib/send_command_to_server.py

tests:
	PYTHONPATH=lib python -m pytest -q test/solution_tests/