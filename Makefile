.DELETE_ON_ERROR:
OS=$(shell uname)
ifeq ($(OS), Darwin)
	DEST=~/Library/Application\ Support/GenIce
else
	DEST=~/.genice
endif

test: iceR.diffr.yap
%.diffr.yap: formats/_Diffr.py formats/contour.py Makefile
	genice $* -r 3 3 3 -f _Diffr[25.0,50.0] > $@
install:
	install -d $(DEST)
	install -d $(DEST)/formats
	install formats/*py $(DEST)/formats
clean:
	-rm $(ALL) *.so *~ */*~ */*/*~ *.o *.gro *.rdf
	-rm -rf build dist
	-rm -rf genice_diffr.egg-info
	-rm -rf */*/__pycache__
