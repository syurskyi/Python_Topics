c_ Solution(object):
  ___ medianSlidingWindow(self, nums, k):
    window = s..(nums[:k])
    medians    # list
    ___ a, b __ z..(nums, nums[k:] + [0]):
      medians.a..((window[k / 2] + window[~(k / 2)]) / 2.)
      window.remove(a)
      bisect.insort(window, b)
    r.. medians
