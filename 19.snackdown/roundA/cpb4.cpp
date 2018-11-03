#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char** argv)
{
  int t, n, m;
  std::cin >> t;

  for (int i=0; i<t; i++) {
    std::cin >> n;
    std::cin >> m;

    int housesI[n * m];
    int housesJ[n * m];
    int nbHouses = 0;
    string line;
    for (int i = 0; i < n; i++) {
      std::cin >> line;
      int j = 0;
      for(string::iterator it = line.begin(); it != line.end(); ++it) {
        if (*it == '1') {
          housesI[nbHouses] = i;
          housesJ[nbHouses] = j;
          nbHouses++;
        };
        j++;
      }
    }
    int nb[n + m - 2];
    for (int i = 0; i < n + m - 2; i++) {
      nb[i] = 0;
    }
    int d;
    int i1, i2, j1, j2;
    for (int i = 0; i < nbHouses - 1; i++) {
      i1 = housesI[i];
      j1 = housesJ[i];
      for (int j = i + 1; j < nbHouses; j++) {
        i2 = housesI[j];
        j2 = housesJ[j];
        d = i2 - i1 + abs(j2 - j1);
        nb[d - 1]++;
      }
    }
    for (int i = 0; i < n + m - 2; i++) {
      cout << nb[i] << " ";
    }
    cout << endl;
  }
  return 0;
}