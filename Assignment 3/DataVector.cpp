#include "DataVector.h"
using namespace std;

DataVector::DataVector(int dimension)
{
    v.resize(dimension);
}

DataVector::~DataVector()
{
    v.clear();
}

DataVector::DataVector(const DataVector &other)
{
    v = other.v;
}

DataVector &DataVector::operator=(const DataVector &other)
{
    v = other.v;
    return *this;
}

void DataVector::setDimension(int dimension)
{
    v.clear();
    v.resize(dimension);
}

int DataVector::getDimension()
{
    return v.size();
}

void DataVector::setVector(vector<double> set)
{
    v = set;
}

vector<double> DataVector::getVector()
{
    return v;
}

DataVector DataVector::operator+(const DataVector &other)
{
    if (v.size() != other.v.size())
    {
        cout << "Addition: ";
        cout << "Unequal dimensions of the vector operands (" << v.size() << ", " << other.v.size() << ")" << endl;
        exit(1);
    }
    DataVector result;
    result.setDimension(v.size());
    for (int i = 0; i < v.size(); i++)
        result.v[i] = v[i] + other.v[i];
    return result;
}

DataVector DataVector::operator-(const DataVector &other)
{
    if (v.size() != other.v.size())
    {
        cout << "Subtraction: ";
        cout << "Unequal dimensions of the vector operands (" << v.size() << ", " << other.v.size() << ")" << endl;
        exit(1);
    }
    DataVector result;
    result.setDimension(v.size());
    for (int i = 0; i < v.size(); i++)
        result.v[i] = v[i] - other.v[i];
    return result;
}

double DataVector::operator*(const DataVector &other)
{
    if (v.size() != other.v.size())
    {
        cout << "Multiplication: ";
        cout << "Unequal dimensions of the vector operands (" << v.size() << ", " << other.v.size() << ")" << endl;
        exit(1);
    }
    double result = 0;
    for (int i = 0; i < v.size(); i++)
        result += v[i] * other.v[i];
    return result;
}

double DataVector::norm(DataVector a)
{
    return sqrt(a * a);
}

double DataVector::dist(DataVector a, DataVector b)
{
    DataVector result = a - b;
    return norm(result);
}
