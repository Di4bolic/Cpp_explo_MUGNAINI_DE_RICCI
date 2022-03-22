#ifndef LIEU_CPP
#define LIEU_CPP

#include "Lieu.h"
#include <iostream>

    Lieu::Lieu(): _nom("SansNom"), _description("SansDescription"),_difficulty(0),_liens({}),_type("normal"){}

    Lieu::Lieu(std::string nom,std::string description,int difficulty,std::vector<int> liens,std::string type):
        _nom(nom),_description(description),_difficulty(difficulty),_liens(liens),_type(type){}

    std::string Lieu::getNom(){
        return _nom;
    }

    std::string Lieu::getDescription(){
        return _description;
    }

    int Lieu::getDifficulty(){
        return _difficulty;
    }

    std::vector<int> Lieu::getDispo(){
        return _liens;
    }

    std::string Lieu::getType(){
        return _type;
    }
        

#endif