class Solution:
    def maxArea(self, height: List[i..]) -> i..:
		maxarea  0
		l  0
		r  len(height)-1

		w___(l<r):
			maxarea  max(maxarea, min(height[l],height[r])*(r-l))
			__(height[l]<height[r]):
				l+1
			else:
				r-1
		return maxarea