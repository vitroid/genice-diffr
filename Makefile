.DELETE_ON_ERROR:
test: iceR.diffr.yap
%.diffr.yap: genice/formats/_Diffr.py genice/formats/contour.py Makefile
	cd genice; genice $* -r 3 3 3 -f _Diffr[25.0,50.0] > ../$@
register:
	./setup.py register -r genice-diffr
pypi:
	./setup.py check
	./setup.py sdist bdist_wheel upload
install:
	make README.rst
	./setup.py install
build.:
	-rm *.so
	-rm -rf build
	python setup.py build_ext --inplace
clean:
	-rm $(ALL) *.so *~ */*~ */*/*~ *.o *.gro *.rdf
	-rm -rf build dist
	-rm -rf PairList.egg-info
	-rm -rf */*/__pycache__


