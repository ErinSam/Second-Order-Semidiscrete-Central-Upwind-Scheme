// interfaceSpeed.h

// Erin Sam Joe | NITK '23 | Mechanical Engg. Major | Electronics & Electrical Engg. Major


#ifndef INTERFACESPEED_H
#define INTERFACESPEED_H


#include <vector>
#include <algorithm>
#include "fluxRelated.h"


// Prototypes
double speedx(const std::vector<double>& fieldEast, const std::vector<double>& fieldWest, 
                bool minim);
double speedy(const std::vector<double>& fieldNorth, const std::vector<double>& fieldSouth, 
                bool minim);


#endif //INTERFACESPEED_H
