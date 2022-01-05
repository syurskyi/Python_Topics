c_ Solution:
    ___ maxArea  height: List[i..]) __ i..:
		maxarea  0
		l  0
		r  l..(height)-1

		w___(l<r):
			maxarea  m..(maxarea, m..(height[l],height[r])*(r-l))
			__(height[l]<height[r]):
				l+1
			____:
				r-1
		r.. maxarea