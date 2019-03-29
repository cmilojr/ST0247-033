function mergesort(m)
  var list left, right, result
  if length(m) ≤ 1
      return m
  else
      var middle = length(m) / 2
      for each x in m up to middle - 1
          add x to left
      for each x in m at and after middle
          add x to right
      left = mergesort(left)
      right = mergesort(right)
      if last(left) ≤ first(right) 
         append right to left
         return left
      result = merge(left, right)
      return result
