
def max_list_iter(int_list):  # must use iteration not recursion
   if int_list == None:
      raise ValueError('The list is empty')
   elif len(int_list) == 0:
      max_int = None
   else:
      max_int = int_list[0]
      for i in range(len(int_list)):
         if int_list[i] > max_int:
            max_int = int_list[i]
   return max_int

def reverse_rec(int_list):   # must use recursion
   if int_list == None:
      raise ValueError('The list is empty')
   elif int_list == []:
      return []
   elif len(int_list) == 1:
      return [int_list[0]]
   else:
      ros = [int_list[-1]]
      templist = reverse_rec(int_list[:-1])
      ros.extend(templist)
      return ros

def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None:
      raise ValueError('The list is empty')
   elif high >= low:
      half = low + (high//2)
      if int_list[half] == target:
         return half
      elif int_list[half] > target:
         return bin_search(target, low, half - 1, int_list)
      else:
         return bin_search(target, half + 1, high, int_list)
   else:
      return None






