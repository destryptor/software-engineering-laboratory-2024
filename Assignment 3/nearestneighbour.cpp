// Name: Sharanya Chakraborty
// Roll No.: 22CS10088

#include <bits/stdc++.h>
#include <chrono>
#include "VectorDataset.h"

using namespace std;

int main()
{

    string fileName; // Reading the dataset file's name
    cout << "Enter Dataset File Name: ";
    cin >> fileName;
    int dataSize; // Asking for the total number of vectors in the dataset
    cout << "Enter Dataset Size: ";
    cin >> dataSize;

    VectorDataset dataset(dataSize);
    dataset.ReadDataset(fileName); // Reading the dataset from the file

    string testFileName;  // Reading the test dataset file's name
    cout << "Enter Test Dataset File Name: ";
    cin >> testFileName;
    int testDataSize; // Asking for the total number of test vectors in the dataset
    cout << "Enter Test Dataset Size: ";
    cin >> testDataSize;

    VectorDataset testDataSet(testDataSize);
    testDataSet.ReadDataset(testFileName); // Reading the dataset from the test file

    int vectorSize = testDataSet.getDimension();
    DataVector testVector(vectorSize); // Creating a vector to be used as the test vector

#ifdef TESTMODE // This mode allows users to test the algorithm on a single vector of their choice (from the dataset)
    cout << "Enter the index of the vector in the dataset to be used as the test vector: ";
    int index;
    cin >> index;
    testVector = dataset.getVectorAtIndex(index);
#endif

    int k;
    cout << "Enter k: "; // Asking for the value of k (number of nearest neighbors)
    cin >> k;

    auto start = chrono::high_resolution_clock::now();
#ifndef TESTMODE // When this mode is not active, the program runs the algorithm on the first 100 vectors of the test dataset. 100 is because our professor told me to do so.
    cout << "Running " << k << "-nearest neighbour algorithm on the dataset for first 100 vectors..." << endl;
    for (int i = 1; i <= 100; i++)
    {
        testVector = testDataSet.getVectorAtIndex(i);
        cout << "Calculating neighbours for " << i << "th vector..." << endl;
        cout << "--------------------------------------------------" << endl;
        VectorDataset result = dataset.knearestneighbor(testVector, k);
    }
#endif

#ifdef TESTMODE
    VectorDataset result = dataset.knearestneighbor(testVector, k);
#endif
    auto stop = chrono::high_resolution_clock::now();

#ifdef TESTMODE
    cout << "The " << k << " nearest neighbors of the test vector are: " << endl;
    result.printDataset();
#endif

    auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);

    int ms = duration.count() % 1000; // Formatting the time taken by the algorithm properly
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
