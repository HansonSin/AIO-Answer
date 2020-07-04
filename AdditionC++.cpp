#include <iostream>
#include <fstream>
using namespace std;

int main() {
  ifstream infile;
  infile.open("addin.txt");
  ofstream outfile;
  outfile.open("addout.txt");
  int a, b;
  infile >> a >> b;
  outfile << a + b;
  infile.close();
  outfile.close();
}
