test:
	PATH=$$HOME/bin/env_python2.6:$$PATH nosetests
clean:
	rm -f $$(find . -name '*.pyc' -o -name '*~')