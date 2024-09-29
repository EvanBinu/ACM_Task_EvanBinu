# Explanation

## Doubly Linked List Initialization
- Created two classes `Node` and `DoubleLinkedList`.
- In the Node class I initialized `data`, `next` and `prev`.
- In the DoubleLinkedList class there are many functions.
- Here the `head` of the DoubleLinkedList is initialized.

## Insert at Begining
- Here the data is added in the `begining` of the `list`.
- A `node` is created and added to the head of the linked list.

## Insert at End
- Here the data is added to the `end`.
- If the List is `empty` a node is `initialized` and data is added.
- A while loop is set to travers to the end of the list 
- When it reaches `itr.next` is `None` a new node with input data is added.

## Get Lenght
- A variable `count` is initialized.
- Using while loop the `length` of the list is calculated.

## Insert At
- It checks if the the index is within the range else is raises and `Exception`.
- If the index is 0 it call the `insert_at_begining` function.
- A variable `itr` is initialized.
- Using while loop the value is added.

## Delete at Begining
- It takes the first node and equates it to the next 

## Delete at End
- First it checks if the list is `empty`.
- If the list is only `single element` then it removes it.
- It goes ot the end using `while loop` and removes the `last element`.

## Delete at
- Same as `insert_at` function it checks the `index`.
- using `while` loop and `if condition` it reaches the required index and removes the element.

## Traverse Forward
- Using the address of the `next` node 
the list is rearranged in `ascending order`.

## Traverse Backward
- Using the address of the `prev` node the list is rearrange in `desending order`.

## Print
- First if the list is empty it is returns a `empty message`.
- A variable `dlstr` is initialized.
- Using `while` loop the data is added to the `dlstr` variable.
- The data is converted to `str`.
