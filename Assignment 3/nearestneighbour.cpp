#include <bits/stdc++.h>
#include "VectorDataset.h"

using namespace std;

int main()
{
    auto start = chrono::high_resolution_clock::now();

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
    cout << "Enter the test vector of dimension " << vectorSize << ": ";
    vector<double> temp;
    for (int i = 0; i < vectorSize; i++)
    {
        cin >> temp[i];
    }
    testVector.setVector(temp);
    int k;
    cout << "Enter k: ";
    cin >> k;
    VectorDataset nearestNeighbors = dataset.knearestneighbor(dataset, testVector, k);

    auto stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);

    cout << "Time taken for nearest neighbor search: " << duration.count() << " milliseconds" << endl;

    return 0;
}
