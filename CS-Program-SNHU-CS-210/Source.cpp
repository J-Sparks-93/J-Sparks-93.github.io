/*
Jeffrey Sparks
Feb 19 2023
CS 210 T3247
Instructor: Cory Thoma*/

#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

int main() {
    map<string, int> item_freq; // map to store item and frequency pairs
    ifstream input_file("CS210_Project_Three_Input_File.txt"); // input file
    ofstream output_file("CS210_Project_Three_Output_File.dat"); // output file to store backup data

    // read items from input file and store frequency in map
    string item;
    while (input_file >> item) {
        ++item_freq[item];
    }

    // write item-frequency pairs to output file for backup
    for (auto i : item_freq) {
        output_file << i.first << ' ' << i.second << endl;
    }

    // display menu options to the user
    int option;
    do {
        cout << "Menu Options:" << endl;
        cout << "1. Find frequency of an item" << endl;
        cout << "2. Print frequency of all items" << endl;
        cout << "3. Print histogram of all items" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> option;
        switch (option) {
        case 1: {
            string item_to_find;
            cout << "Enter the item to find frequency of: ";
            cin >> item_to_find;
            cout << item_to_find << " appears " << item_freq[item_to_find] << " times." << endl;
            break;
        }
        case 2: {
            cout << "Item Frequency" << endl;
            for (auto i : item_freq) {
                cout << i.first << ' ' << i.second << endl;
            }
            break;
        }
        case 3: {
            cout << "Item Histogram" << endl;
            for (auto i : item_freq) {
                cout << i.first << " ";
                for (int j = 0; j < i.second; ++j) {
                    cout << "*";
                }
                cout << endl;
            }
            break;
        }
        case 4: {
            break;
        }
        default: {
            cout << "Invalid option. Enter again." << endl;
            break;
        }
        }
    } while (option != 4);

    return 0;
}
