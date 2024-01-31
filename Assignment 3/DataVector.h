// Name: Sharanya Chakraborty
// Roll No. : 22CS10088
#include <bits/stdc++.h>
using namespace std;

/* The DataVector class represents a mathematical vector of doubles in a specified dimension.
It supports basic vector operations such as addition, subtraction, dot product,
norm calculation, and distance calculation between two vectors.*/

class DataVector
{
    vector<double> v; // Vector to store the elements

public:
    // Constructor: Initializes an empty vector with the specified dimension (default is 0).
    DataVector(int dimension = 0);

    // Destructor
    ~DataVector();

    // Copy Constructor: Creates a new vector as a copy of another vector.
    DataVector(const DataVector &other);

    // Copy Assignment Operator: Assigns the contents of another vector to this vector.
    DataVector &operator=(const DataVector &other);

    // setDimension: Sets the dimension of the vector.
    void setDimension(int dimension = 0);

    // getDimension: Returns the dimension of the vector.
    int getDimension();

    // setVector: Sets the elements of the vector using a provided vector.
    void setVector(vector<double> set);

    // getVector: Returns the vector as a vector of doubles.
    vector<double> getVector();

    // operator+: Overloaded addition operator for vector addition.
    DataVector operator+(const DataVector &other);

    // operator-: Overloaded subtraction operator for vector subtraction.
    DataVector operator-(const DataVector &other);

    // operator*: Overloaded multiplication operator for dot product calculation.
    double operator*(const DataVector &other);

    // norm: Calculates the Euclidean norm of a vector.
    double norm(DataVector a);

    // dist: Calculates the Euclidean distance between two vectors.
    double dist(DataVector a, DataVector b);
};