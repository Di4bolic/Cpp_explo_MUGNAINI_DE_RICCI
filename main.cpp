#include "Lieu.cpp"

#include <iostream>
#include <string>


int main(){

    int endurance;
    endurance = 100;
    bool win;
    win = false;

    Lieu * lieu1 = new Lieu("Town","Une ville plutôt plaisible",1,{2,3},"normal");
    Lieu * lieu2 = new Lieu("Forest","Une forêt mystériieuse et dangereuse",10,{1,3},"refuge");
    Lieu * lieu3 = new Lieu("Sea","Une mer qui semble calme",12,{1,2},"normal");

    std::cout<<lieu1->getNom()<<std::endl;
    std::cout<<lieu2->getNom()<<std::endl;
    std::cout<<lieu3->getNom()<<std::endl;

    // Je voulais faire un vecteur ( lieuxDispo ) contenant les lieux disponibles
    // Pour avoir lieu1 j'aurais fait lieux[1] , cependant je ne sait pas quel est le type objet donc comment déclarer le vecteur
    // Je voulais faire une variable ( lieuActuel ) contenant le lieu actuel ,cependant je ne sait pas quel est le type objet donc comment déclarer la variable
    
    void deplacement(){

        int lieuVoulu;
        std::cin >> lieuVoulu;
        for (size_t i = 0; i < 2; i++)
        {
            // Je test si le lieu voulu est bien disponible
            if (lieuVoulu == lieuActuel->getDispo()[i])
            {
                // En faisant attention si l'endurance n'est pas inférieur à 0
                if (endurance - lieuxDispo[lieuVoulu]->getDifficulty() >= 0)
                {
                    lieuActuel = lieuxDispo[lieuVoulu];
                    endurance -= lieuActuel->getDifficulty();
                }
                else{
                    std::cout<<"Pas assez d'endurance"<<std::endl;
                }
            }
            else{
                std::cout<<"Le déplacement est impossible car le lieu n'est pas disponible"<<std::endl;
            }
        }
    }

    while (/*win == false*/) //On a pas d'objectif dans le jeu donc c'est bizarre
    {
        int action;
        std::cin >> action;
        if (action == 1)
        {
            deplacement();
        }
        else{
            if (lieuActuel->getType()=="refuge")
            {
                endurance += 50;
                if (endurance > 100)
                {
                    endurance = 100
                }
            }
        }
    }
    
        
    









    
    



    return 0;
}