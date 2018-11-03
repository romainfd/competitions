#include <iostream>
#include <vector>
#include "img_processing.h"
#include "math.h"
#include "dirent.h"
using namespace std;

// TO USE to_string
#include <string>
#include <sstream>
template <typename T>
std::string toString(T val)
{
    std::stringstream stream;
    stream << val;
    return stream.str();
}

// infinity
double infinity = 1E+30;

const int deltaSize = 4;
const int minSize = 8;
const string imageFolder = "/usr/local/INF442-2018/P5/";
const string repo = "app";
const string repo2 = "test";

// Parameters set in the args
double normalisation = 1;
int printDebug = 0;

// Affichage d'une matrice de façon alignée pour des valeurs entre -9 et 99
void displayMatrix(vector<vector<int> >& matrix) {
    // we only use the reference to avoid a useless copy
    for (unsigned int i = 0; i < matrix.size(); i++) {
        for (unsigned int j = 0; j < matrix[0].size(); j++) {
            if (matrix[i][j] >= 0 and matrix[i][j] < 20) {
                cout << " "; // pour tout avoir aligné pour des valeurs entre -9 et 99
            }
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}
