#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <map>

using namespace std;

vector<pair<string, string>> galeShapley(
    map<string, vector<string>>& male_prefs,
    map<string, vector<string>>& female_prefs
) {
    map<string, vector<string>> mp = male_prefs;
    map<string, pair<map<string, int>, pair<int, string>>> fp;
    map<string, int> curr_pair;

    for (auto& p : female_prefs) {
        fp[p.first] = {map<string, int>(), {-1, ""}};
        fp[p.first].first = map<string, int>();
        for (int i = 0; i < p.second.size(); i++) {
            fp[p.first].first[p.second[i]] = i;
        }
    }
    
    for (auto& p : male_prefs) {
        curr_pair[p.first] = 0;
    }

    while (mp.size() > 0) {
        map<string, vector<string>> next;
        for (auto& p : mp) {
            string male = p.first;
            int pointer = curr_pair[male];
            string female = p.second[pointer];

            if (fp[female].second.first == -1) {
                fp[female].second = {fp[female].first[male], male};
            } else if (fp[female].second.first != -1 && fp[female].first[male] < fp[female].second.first) {
                string free_male = fp[female].second.second;
                next[free_male] = male_prefs[free_male];
                curr_pair[free_male]++;
                fp[female].second = {fp[female].first[male], male};
            } else {
                next[male] = male_prefs[male];
                curr_pair[male]++;
            }
        }
        mp = next;
    }
    vector<pair<string, string>> pairings;
    for (auto& p : male_prefs) {
        pairings.push_back({p.first, p.second[curr_pair[p.first]]});
    }
    return pairings;
}

int main() {
    map<string, vector<string>> male_prefs;
    map<string, vector<string>> female_prefs;

    male_prefs["A"] = {"O", "M", "N", "L", "P"};
    male_prefs["B"] = {"P", "N", "M", "L", "O"};
    male_prefs["C"] = {"M", "P", "L", "O", "N"};
    male_prefs["D"] = {"P", "M", "O", "N", "L"};
    male_prefs["E"] = {"O", "L", "M", "N", "P"};

    female_prefs["L"] = {"D", "B", "E", "C", "A"};
    female_prefs["M"] = {"B", "A", "D", "C", "E"};
    female_prefs["N"] = {"A", "C", "E", "D", "B"};
    female_prefs["O"] = {"D", "A", "C", "B", "E"};
    female_prefs["P"] = {"B", "E", "A", "C", "D"};

    vector<pair<string, string>> pairings = galeShapley(male_prefs, female_prefs);
    cout << "Derived pairings:" << endl;
    for (auto& p : pairings) {
        cout << p.first << "<->" << p.second << endl;
    }
    return 0;
}