newenv: # Generate env and get dependencies
	@bash -c 'echo ;\
	echo python3 -m venv .venv ;\
	python3 -m venv .venv ;\
	echo source .venv/bin/activate ;\
	source .venv/bin/activate ;\
	echo pip3 install -r requirements.txt ;\
	pip3 install -r requirements.txt ;\
	echo source .venv/bin/activate ;\
	source .venv/bin/activate ;\
	'