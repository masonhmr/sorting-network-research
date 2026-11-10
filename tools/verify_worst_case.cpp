#include <algorithm>
#include <array>
#include <cstdint>
#include <iomanip>
#include <fstream>
#include <iostream>
#include <utility>
#include <vector>

// Read the archived baseline and contribution supplied by verify_all.py.
int main(int argc, char** argv) {
  if(argc != 2) {std::cerr << "Usage: verify_worst_case networks.txt\n"; return 3;}
  std::ifstream input_file(argv[1]);
  using P = std::pair<int,int>;
  std::vector<std::vector<P>> nets(2);
  for(auto &net:nets) for(int k=0;k<29;++k) {
    int a,b;
    if(!(input_file >> a >> b) || a<0 || a>=b || b>=10) return 3;
    net.emplace_back(a,b);
  }
  std::string extra;
  if(input_file >> extra) return 3;
  for (int id=0;id<2;++id) {
    const auto &net=nets[id];
    std::array<int,10> input={0,1,2,3,4,5,6,7,8,9}, witness{};
    std::uint64_t total=0,count=0;int worst=-1;
    do {
      auto x=input;int swaps=0;
      for(auto [a,b]:net) if(x[a]>x[b]) {std::swap(x[a],x[b]);++swaps;}
      if(!std::is_sorted(x.begin(),x.end())) {std::cerr<<"Unsorted output\n";return 1;}
      if(swaps>worst){worst=swaps;witness=input;}
      total+=swaps;++count;
    } while(std::next_permutation(input.begin(),input.end()));
    if(count!=3628800 || worst!=(id==0?21:20)) return 2;
    std::cout<<(id==0?"baseline":"contribution")<<": permutations="<<count<<" max="<<worst
      <<" total="<<total<<" average="<<std::setprecision(12)<<double(total)/count<<" witness=";
    for(int v:witness)std::cout<<v<<' ';std::cout<<'\n';
  }
}

