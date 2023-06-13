#include "dog.h"
#include<iostream>

Dog::Dog(){
    cout<<"Empty Dog created" <<endl;
}

Dog::Dog(int id, string name): id(id),
name(name){
    cout<<"Dog created";
}