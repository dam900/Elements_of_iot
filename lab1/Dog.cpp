#include <iostream>
#include "Animal.cpp"

class Dog : public Animal {
public:
    void make_sound() const override {
        std::cout << "Woof!" << std::endl;
    }
};

extern "C" {
    Animal* create_animal() {
        return new Dog();
    }
}