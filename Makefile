# Makefile

OBJS = obj/fluxRelated.o obj/converter.o obj/interfaceSpeed.o obj/minmodForVLLim.o obj/meshClass.o obj/configurations.o
CC = g++ 
CFLAGS = -c -Wall 
LFLAGS = 

EIGEN = -I lib/Eigen/
PYBIND = -fPIC -I /usr/include/python3.8/ $(python3 -m pybind11 --includes)


lib/meshClass.so : $(OBJS)
	$(CC) -O3 -Wall -shared -fopenmp $(PYBIND) $(EIGEN) $(OBJS) -o lib/meshClass.so

obj/meshClass.o : src/meshClass.cc src/meshClass.h src/fluxRelated.h src/converter.h src/minmodForVLLim.h src/interfaceSpeed.h src/configurations.h
	$(CC) $(CFLAGS) -fopenmp $(PYBIND) $(EIGEN) src/meshClass.cc -o obj/meshClass.o

obj/configurations.o : src/configurations.cc src/configurations.h src/converter.h
	$(CC) $(CFLAGS) src/configurations.cc -o obj/configurations.o

obj/interfaceSpeed.o : src/interfaceSpeed.cc src/interfaceSpeed.h src/fluxRelated.h
	$(CC) $(CFLAGS) $(EIGEN) src/interfaceSpeed.cc -o obj/interfaceSpeed.o

obj/fluxRelated.o : src/fluxRelated.cc src/fluxRelated.h
	$(CC) $(CFLAGS) $(EIGEN) src/fluxRelated.cc -o obj/fluxRelated.o

obj/converter.o : src/converter.cc src/converter.h
	$(CC) $(CFLAGS) src/converter.cc -o obj/converter.o  

obj/minmodForVLLim.o : src/minmodForVLLim.cc src/minmodForVLLim.h
	$(CC) $(CFLAGS) src/minmodForVLLim.cc -o obj/minmodForVLLim.o

clean : 
	rm obj/*.o lib/*.so

plotLatest : 
	python3 ./bin/postProcess.py 0

saveAll : 
	python3 ./bin/postProcess.py x
