#include "VectorDataset.h"
#include <chrono>
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

vector<DataVector> VectorDataset::getSet()
{
    return set;
}

DataVector VectorDataset::getVectorAtIndex(int index)
{
    return set[index];
}

void VectorDataset::ReadDataset(string fileName)
{
    cout << "Reading dataset..." << endl;
    auto start = chrono::high_resolution_clock::now();
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
        auto stop = chrono::high_resolution_clock::now();

        auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);
        int ms = duration.count() % 1000;
        int s = (duration.count() / 1000) % 60;
        int m = (duration.count() / (1000 * 60)) % 60;
        int h = (duration.count() / (1000 * 60 * 60)) % 24;

        cout << "Time taken to read the dataset: ";
        if (h > 0)
            cout << h << "h ";
        if (m > 0 || h > 0)
            cout << m << "m ";
        if (s > 0 || m > 0 || h > 0)
            cout << s << "s ";
        cout << ms << "ms" << endl;
    }
    else
    {
        cout << "Unable to open file: " << fileName << endl;
    }
}

VectorDataset VectorDataset::knearestneighbor(DataVector a, int k)
{
    VectorDataset result(k);

    vector<pair<double, int>> distancesAndIndices;

    for (int i = 0; i < set.size(); ++i)
    {
        double distance = a.dist(a, set[i]);
        distancesAndIndices.push_back({distance, i});
    }

    sort(distancesAndIndices.begin(), distancesAndIndices.end());

    for (int i = 0; i < k; ++i)
    {
        int index = distancesAndIndices[i].second;
        result.set[i] = set[index];
    }

    return result;
}

void VectorDataset::printDataset()
{
    for (int i = 0; i < set.size(); i++)
    {
        for (int j = 0; j < set[i].getDimension(); j++)
            cout << set[i].getVector()[j] << " ";
        cout << endl;
    }
}