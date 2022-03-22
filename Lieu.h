#ifndef LIEU_H
#define LIEU_H

#include <string>
#include <vector>

class Lieu{

    protected:

        std::string _nom;
        std::string _description;
        int _difficulty;
        std::vector<int> _liens;
        std::string _type;
        
    public:

        Lieu();
        Lieu(std::string nom,std::string description,int difficulty,std::vector<int> liens,std::string type);

        std::string getNom();
        // Donne le nom du lieu
        
        std::string getDescription();
        // Donne la description du lieu

        int getDifficulty();
        // Donne la description du lieu

        std::string getType();
        // Donne la description du lieu

        std::vector<int> getDispo();
        // Donne la description du lieu

};

#endif