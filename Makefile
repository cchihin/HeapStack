CPP = g++
SRC = serial.cpp 
SRC_STK = serial-stack.cpp
OBJ = $(SRC:.cpp=.o)
OBJ_STK = $(SRC_STK:.cpp:.o)

all: serial serial-stack clean

serial: $(OBJ)
	$(CPP) $(OBJ) -o serial

serial.o: $(SRC)
	$(CPP) -c $(SRC) -o $(OBJ)

serial-stack: $(OBJ_STK)
	$(CPP) $(OBJ_STK) -o serial-stack

serial-stack.o: $(SRC_STK)
	$(CPP) -c $(SRC_STK) -o $(OBJ_STK)

clean:
	rm $(OBJ)
