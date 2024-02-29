// Name: Sharanya Chakraborty
// Roll No.: 22CS10088

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

    getline(file, line); // skip the first line containing serial numbers

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
        exit(-1);
    }
}

VectorDataset VectorDataset::knearestneighbor(DataVector a, int k)
{
    VectorDataset result(k);

    // Calculating the distance of the given vector from all the vectors in the dataset and storing them in a vector of pairs
    vector<pair<double, int>> distancesAndIndices;

    for (int i = 0; i < set.size(); ++i)
    {
        double distance = a.dist(a, set[i]);
        distancesAndIndices.push_back({distance, i});
    }

    // Sorting the vector of pairs in ascending order of distance
    sort(distancesAndIndices.begin(), distancesAndIndices.end());

    // Storing the k-nearest neighbors in the result vector
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