CPP = g++
SRC = serial.cpp 

all: serial clean

serial: $(OBJ)
	$(CPP) $(OBJ) -o serial

serial.o: $(SRC)
	$(CPP) -c $(SRC) -o $(OBJ)

clean:
	rm $(OBJ)
