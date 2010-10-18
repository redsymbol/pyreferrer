TWO2THREE=2to3-2.6
test:
	PATH=$$HOME/bin/env_python2.6:$$PATH nosetests
	PATH=$$HOME/bin/env_python2.7:$$PATH nosetests

# Pyreferrer is pretty straightforwardly updateable to Python 3 using 2to3.
# To run tests, use a py3k-capable nose, or just "python3.2 tests.py" should work.

test3k:
	PATH=$$HOME/bin/env_python3.2:$$PATH nosetests

clean:
	rm -f $$(find . -name '*.pyc' -o -name '*~')