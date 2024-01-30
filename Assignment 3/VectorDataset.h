#include "DataVector.h"
using namespace std;

class VectorDataset
{
    vector<DataVector> set;

public:
    VectorDataset(int numVectors);
    ~VectorDataset();
    int getDimension();
    vector<DataVector> getSet();
    DataVector getVectorAtIndex(int index);
    void ReadDataset(string fileName);
    VectorDataset knearestneighbor(DataVector a, int k);
    void printDataset();
};
