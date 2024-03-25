#include <iostream>

class Animal {
public:
    virtual void make_sound() const {
        std::cout << "Generic animal sound" << std::endl;
    }
};