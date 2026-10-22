class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxwater = 0;
        int l = 0;
        int r = height.size()-1;
        while(l<r){
            int w = r-l;
            int h = min(height[l], height[r]);
            int water = w*h;

            maxwater = max(water, maxwater);

            if(height[l]>height[r]){
                r--;
            }else{
                l++;
            }
        }
        return maxwater;
    }
};