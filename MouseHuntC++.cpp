#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
    ifstream infile;
    infile.open("mousein.txt");
    int xlis[8] = {-1, -1, -1, -1, -1, -1, -1, -1};
    int ylis[8] = {-1, -1, -1, -1, -1, -1, -1, -1};
    for (int i = 0; i < 8; i++) {
        string instr1, instr2;
        infile >> instr1 >> instr2;
        int in1 = stoi(instr1);
        int in2 = stoi(instr2);
        xlis[i] = in1;
        ylis[i] = in2;
    }
    infile.close();
    ofstream outfile;
    outfile.open("mouseout.txt");
    if (count(xlis, xlis + 8, *(min_element(xlis, xlis + 8))) == 4) {
        outfile << "W";
    } else if (count(xlis, xlis + 8, *(max_element(xlis, xlis + 8))) == 4) {
        outfile << "E";
    } else if (count(ylis, ylis + 8, *(min_element(ylis, ylis + 8))) == 4) {
        outfile << "S";
    } else if (count(ylis, ylis + 8, *(max_element(ylis, ylis + 8))) == 4) {
        outfile << "N";
    }
    outfile.close();
}
