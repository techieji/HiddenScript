#include <vector>
#include <string>
#include <direct.h>
#include <filesystem>

using namespace std;

namespace fs = std::filesystem;

class Tree {
    vector<Tree> branches;
    vector<fs::directory_entry> files;
public:
    Tree(fs::path startpath);
    vector<fs::path> FindExtension(string ex);
};

Tree::Tree(fs::path startpath) {
    for (const auto & file : fs::directory_iterator(startpath)) {
        if (file.is_directory()) {
            branches.push_back(Tree(file.path));
        }
        else {
            files.push_back(file.path);
        }
    }
}

vector<fs::path> Tree::FindExtension(string ex) {
    vector<fs::path> returnval;
    for (const auto & file : files) {
        if (file.path.extension().string() == ex) {
            returnval.push_back(file.path);
        }
    }
    for (auto & dir : branches) {
        vector<fs::path> retvec = dir.FindExtension(ex);
        returnval.insert(returnval.end(), retvec.begin(), retvec.end());
    }
    return returnval;
}