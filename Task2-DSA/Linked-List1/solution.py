def removeDuplicates(llist):   
    itr = llist
    while itr:
      if itr.next and itr.data == itr.next.data:
        itr.next = itr.next.next
      else:
        itr = itr.next
    return llist