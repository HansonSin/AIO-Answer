#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
  ifstream infile;
  infile.open("vasesin.txt");
  string ni;
  infile >> ni;
  int n = stoi(ni);
  infile.close();
  ofstream outfile;
  outfile.open("vasesout.txt");
  if (n >= 6) {
    string ans = "1 2 " + to_string(n - 3);
    outfile << ans;
  } else {
    outfile << "0 0 0";
  }
}
