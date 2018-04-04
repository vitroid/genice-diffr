.DELETE_ON_ERROR:
OS=$(shell uname)
ifeq ($(OS), Darwin)
	DEST=~/Library/Application\ Support/GenIce
else
	DEST=~/.genice
endif

test: iceR.diffr.yap
%.diffr.yap: genice/formats/_Diffr.py genice/formats/contour.py Makefile
	cd genice; genice $* -r 3 3 3 -f _Diffr[25.0,50.0] > ../$@
install:
	install -d $(DEST)
	install -d $(DEST)/formats
	install genice/formats/*py $(DEST)/formats
clean:
	-rm $(ALL) *.so *~ */*~ */*/*~ *.o *.gro *.rdf
	-rm -rf build dist
	-rm -rf genice_diffr.egg-info
	-rm -rf */*/__pycache__
