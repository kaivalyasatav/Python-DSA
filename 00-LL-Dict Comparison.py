head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}
print(head['next']['next']['value'])

#THis will run only with a linked list
# print(my_linked_list.head.next.next.value)