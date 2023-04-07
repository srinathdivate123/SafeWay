#include <vector>

using namespace std;



    int maxProfit(vector<int>& prices) {

        int start = 0, end = prices.size()-1;

        int maxprofit = 0;

        while(end!=start){

            maxprofit = max(prices[end] - prices[start],maxprofit);


            if(prices[start+1] <= prices[start]){
                start+=1;
                if(prices[end-1] >= prices[end]){

                    end-=1;

                }
            }else{
                if(prices[end-1] >= prices[end]){
                    end-=1;
                }else{
                    start+=1;
                }
            }
        
        }

        return maxprofit;
        
    }