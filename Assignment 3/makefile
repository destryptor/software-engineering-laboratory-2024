CC = gcc
CFLAGS = -O2 -Wall -I.
LIBNAME = libvector.a
LIBOBJS = DataVector.o VectorDataset.o

all: $(LIBNAME)

$(LIBNAME): $(LIBOBJS)
	ar rcs $(LIBNAME) $(LIBOBJS)

DataVector.o : DataVector.h
VectorDataset.o : VectorDataset.h

clean:
	rm -f $(LIBNAME) $(LIBOBJS)

