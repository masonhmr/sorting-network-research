#include <algorithm>
#include <array>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

// Network sequences transcribed from upstream commit 9187435 (see docs/EVIDENCE.md).
int main() {
  using P = std::pair<int,int>;
  const std::vector<P> suffix={{1,2},{3,5},{4,6},{7,8},{2,3},{4,5},{6,7},{3,4},{5,6}};
  std::vector<std::vector<P>> nets={
    {{0,7},{1,6},{2,9},{3,8},{4,5},{0,3},{1,4},{5,8},{6,9},{0,2},{3,6},{7,9},{0,1},{2,4},{5,7},{8,9},{1,3},{2,5},{4,7},{6,8}},
    {{0,7},{1,8},{2,3},{4,5},{6,9},{0,4},{1,2},{3,9},{5,8},{0,6},{3,4},{7,9},{0,1},{2,6},{5,7},{8,9},{1,3},{2,5},{4,8},{6,7}}
  };
  for (int id=0;id<2;++id) {
    auto net=nets[id];net.insert(net.end(),suffix.begin(),suffix.end());
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
