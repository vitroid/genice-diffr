.DELETE_ON_ERROR:
test: iceR.diffr.yap
%.diffr.yap: genice/formats/_Diffr.py genice/formats/contour.py Makefile
	cd genice; genice $* -r 3 3 3 -f _Diffr[25.0,50.0] > ../$@
register:
	./setup.py register -r genice-diffr
check:
	./setup.py check
build.:
	-rm *.so
	-rm -rf build
	./setup.py build_ext --inplace
install:
	./setup.py install
pypi:
	./setup.py check
	./setup.py sdist bdist_wheel upload
clean:
	-rm $(ALL) *.so *~ */*~ */*/*~ *.o *.gro *.rdf
	-rm -rf build dist
	-rm -rf PairList.egg-info
	-rm -rf */*/__pycache__


