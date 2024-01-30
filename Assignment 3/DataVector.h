#include <bits/stdc++.h>
using namespace std;

class DataVector
{
    vector<double> v;

public:
    DataVector(int dimension = 0);
    ~DataVector();
    DataVector(const DataVector &other);
    DataVector &operator=(const DataVector &other);
    void setDimension(int dimension = 0);
    int getDimension();
    void setVector(vector<double> set);
    vector<double> getVector();
    DataVector operator+(const DataVector &other);
    DataVector operator-(const DataVector &other);
    double operator*(const DataVector &other);
    double norm(DataVector a);
    double dist(DataVector a, DataVector b);
};
