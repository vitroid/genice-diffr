.DELETE_ON_ERROR:
OS=$(shell uname)
ifeq ($(OS), Darwin)
	DEST=~/Library/Application\ Support/GenIce
else
	DEST=~/.genice
endif

test: iceR.diffr.yap
%.diffr.yap: genice_diffr/formats/_Diffr.py Makefile
	genice $* -r 3 3 3 -f _Diffr[25.0,50.0] > $@
install:
	./setup.py install
clean:
	-rm $(ALL) *~ */*~ *.yap
	-rm -rf build dist *.egg-info
	-find . -name __pycache__ | xargs rm -rf
