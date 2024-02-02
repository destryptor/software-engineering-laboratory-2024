CC = gcc
CFLAGS = -O2 -Wall -I.
LIBNAME = libvector.a
LIBOBJS = DataVector.o VectorDataset.o

run: $(LIBNAME)
	g++ nearestneighbour.cpp -o nearestneighbour.out -L. -lvector; ./nearestneighbour.out

$(LIBNAME): $(LIBOBJS)
	ar rcs $(LIBNAME) $(LIBOBJS)

DataVector.o : DataVector.h
VectorDataset.o : VectorDataset.h

clean:
	rm -f $(LIBNAME) $(LIBOBJS) nearestneighbour.out

