test:
	PATH=$$HOME/bin/env_python2.6:$$PATH nosetests
	PATH=$$HOME/bin/env_python2.7:$$PATH nosetests
clean:
	rm -f $$(find . -name '*.pyc' -o -name '*~')