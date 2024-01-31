// Name: Sharanya Chakraborty
// Roll No.: 22CS10088
#include "DataVector.h"
using namespace std;

/* The VectorDataset class represents a dataset of DataVectors.
It provides functionalities to read a dataset from a csv file, retrieve individual vectors, find k-nearest neighbors for a given vector, and print the entire dataset. */
class VectorDataset
{
    vector<DataVector> set; // Vector to store DataVectors

public:
    // Constructor: Initializes the dataset with a specified number of vectors.
    VectorDataset(int numVectors);

    // Destructor
    ~VectorDataset();

    // getDimension: Returns the dimension of the vectors in the dataset.
    int getDimension();

    // getSet: Returns the entire dataset as a vector of DataVectors.
    vector<DataVector> getSet();

    // getVectorAtIndex: Returns the DataVector at a specified index in the dataset.
    DataVector getVectorAtIndex(int index);

    // ReadDataset: Reads a dataset from a csv file and populates the vector set.
    void ReadDataset(string fileName);

    // knearestneighbor: Finds the k-nearest neighbors for a given vector in the dataset.
    VectorDataset knearestneighbor(DataVector a, int k);

    // printDataset: Prints the entire dataset.
    void printDataset();
};
