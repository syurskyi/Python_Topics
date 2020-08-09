c_ Solution:
    ___ maxArea(, height: L.. in.) -> int:
		maxarea _ 0
		l _ 0
		r _ le.(height)-1

		w___(l<r
			maxarea _ ma.(maxarea, min(height[l],height[r])*(r-l))
			__(height[l]<height[r]
				l+_1
			____
				r-_1
		r_ maxarea