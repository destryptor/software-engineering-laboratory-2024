#include <bits/stdc++.h>
#include <chrono>
#include "VectorDataset.h"

using namespace std;

int main()
{

    string fileName;
    cout << "Enter Dataset File Name: ";
    cin >> fileName;
    int dataSize;
    cout << "Enter Dataset Size: ";
    cin >> dataSize;

    VectorDataset dataset(dataSize);
    dataset.ReadDataset(fileName);

    int vectorSize = dataset.getDimension();
    DataVector testVector(vectorSize);

#ifdef MANUALTESTVECTOR
    cout << "Enter the test vector of dimension " << vectorSize << ": ";
    vector<double> temp(vectorSize);
    for (int i = 0; i < vectorSize; i++)
        cin >> temp[i];
    testVector.setVector(temp);
#endif
#ifndef ALLVECTORS
    cout << "Enter the index of the vector in the dataset to be used as the test vector: ";
    int index;
    cin >> index;
    testVector = dataset.getVectorAtIndex(index);
#endif

    int k;
    cout << "Enter k: ";
    cin >> k;

    auto start = chrono::high_resolution_clock::now();
#ifdef ALLVECTORS
    for (DataVector vector : dataset.getSet())
    {
        dataset.knearestneighbor(vector, k);
    }
#endif

    VectorDataset result = dataset.knearestneighbor(testVector, k);
    auto stop = chrono::high_resolution_clock::now();

#ifndef ALLVECTORS
    cout << "The " << k << " nearest neighbors of the test vector are: " << endl;
    result.printDataset();
#endif

    auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);

    int ms = duration.count() % 1000;
    int s = (duration.count() / 1000) % 60;
    int m = (duration.count() / (1000 * 60)) % 60;
    int h = (duration.count() / (1000 * 60 * 60)) % 24;

    cout << "Time taken: ";
    if (h > 0)
        cout << h << "h ";
    if (m > 0 || h > 0)
        cout << m << "m ";
    if (s > 0 || m > 0 || h > 0)
        cout << s << "s ";
    cout << ms << "ms";

    return 0;
}
