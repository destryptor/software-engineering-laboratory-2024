#include "DataVector.h"
using namespace std;

class VectorDataset
{
    vector<DataVector> set;

public:
    VectorDataset(int numVectors);
    ~VectorDataset();
    int getDimension();
    DataVector getVectorAtIndex(int index);
    void ReadDataset(string fileName);
    VectorDataset knearestneighbor(VectorDataset set, DataVector a, int k);
};
