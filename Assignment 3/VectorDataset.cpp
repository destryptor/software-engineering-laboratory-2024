#include "VectorDataset.h"
using namespace std;

VectorDataset::VectorDataset(int numVectors)
{
    set.resize(numVectors);
}

VectorDataset::~VectorDataset()
{
    set.clear();
}

int VectorDataset::getDimension()
{
    return set[0].getDimension();
}

DataVector VectorDataset::getVectorAtIndex(int index)
{
    return set[index];
}

void VectorDataset::ReadDataset(string fileName)
{
    ifstream file(fileName);
    string line;

    if (file.is_open())
    {
        int index = 0;
        while (getline(file, line) && index < set.size())
        {
            stringstream ss(line);
            string value;
            vector<double> vectorData;

            while (getline(ss, value, ','))
            {
                vectorData.push_back(stod(value));
            }

            set[index].setVector(vectorData);
            index++;
        }
        file.close();
    }
    else
    {
        cout << "Unable to open file: " << fileName << endl;
    }
}

VectorDataset VectorDataset::knearestneighbor(VectorDataset set, DataVector a, int k)
{
    VectorDataset result(k);

    return result;
}
