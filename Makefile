CPP = g++
SRC = heapstack.cpp 
OBJ = $(SRC:.cpp=.o)

all: heapstack clean

heapstack: $(OBJ)
	$(CPP) $(OBJ) -o heapstack

heapstack.o: $(SRC)
	$(CPP) -c $(SRC) -o $(OBJ)

clean:
	rm $(OBJ)
