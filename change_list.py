def change_list(lst):
  lst.pop(0)
  lst.pop(-2)
  lst.append(5)
  lst.sort()
  lst.reverse()
  return lst, len(lst)
