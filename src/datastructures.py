
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, name, edad, suerte):
        # fill this method and update the return
        member ={
            "name":name,
            "last_name":self.last_name,
            "age": edad,
            "lucky_numbers":suerte,
            "id": self._generateId()
        }
        self._members.append(member)
        return self._members


    def delete_member(self, id):
        # fill this method and update the return
        delete = list(filter(lambda item: item["id"] != id, self._members))
        self._members.clear()
        self._members.extend(delete)

        return self._members



    def get_member(self, id):
        # fill this method and update the return
        specific_dict = [item for item in self._members if item['id'] == id]
        if specific_dict:
            return (specific_dict[0])
        else:
            return ("No se encontro el miembro en la lista.")
        
        
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
