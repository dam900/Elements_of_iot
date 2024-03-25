build:
	@g++ -c -fPIC Animal.cpp   # Compile Animal.cpp to object file
	@g++ -c -fPIC Dog.cpp      # Compile Dog.cpp to object file
	@g++ -c -fPIC main.cpp     # Compile main.cpp to object file

	@g++ -shared -o Dog.so Dog.o Animal.o              # Link Dog.o and Animal.o into shared library
	@g++ main.o -o build.out -ldl   
	@rm Animal.o main.o Dog.o

run: build
	@echo "Running ./build.out" 
	@./build.out

clean:
	@rm Dog.so build.out