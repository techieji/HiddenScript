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