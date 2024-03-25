#include <iostream>
#include <dlfcn.h> // For dynamic loading
#include "Animal.cpp"

// Define a function pointer type for the factory function
typedef Animal* (*CreateAnimalFn)();

int main() {
    // Load the shared library dynamically
    void* handle = dlopen("./Dog.so", RTLD_LAZY);
    if (!handle) {
        std::cerr << "Failed to load the shared library: " << dlerror() << std::endl;
        return 1;
    }

    // Get the function pointer to the factory function
    CreateAnimalFn createDog = reinterpret_cast<CreateAnimalFn>(dlsym(handle, "create_dog"));
    if (!createDog) {
        std::cerr << "Failed to get the factory function: " << dlerror() << std::endl;
        dlclose(handle);
        return 1;
    }

    // Create Animal object using factory function from shared library
    Animal* animal = createDog();
    if (!animal) {
        std::cerr << "Failed to create the Animal object." << std::endl;
        dlclose(handle);
        return 1;
    }

    // Call the method using polymorphism
    animal->make_sound();

    // Remember to free the memory allocated by the shared library
    delete animal;
    animal = nullptr;

    // Unload the shared library
    dlclose(handle);

    return 0;
}