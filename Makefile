publish:
	@python setup.py sdist bdist_wheel
	@twine upload --config-file .pypirc --repository local dist/*
