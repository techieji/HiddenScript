#include <vector>
#include <string>
#include <direct.h>
#include <filesystem>

using namespace std;
using namespace std::filesystem;

class Tree {
    vector<Tree> branches;
    vector<path> files;
public:
    Tree(string startpath);
};

Tree::Tree(string startpath) {
    current_path(startpath);
}