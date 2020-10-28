
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

    def add_member(self, member):
        # fill this method and update the return
        if 'id' in member:
            member['last_name'] = self.last_name
            self._members.append(member)
        else:
            member['id'] = self._generateId()
            member['last_name'] = self.last_name
            self._members.append(member)
        return None

    def delete_member(self, id):
        # fill this method and update the return
        for person in range(len(self._members)):
            print("THIS IS PERSON", person)
            print("THIS IS MEMBERS", self._members)
            if self._members[person]['id'] == id:
                self._members.pop(person)
        return None

    def get_member(self, id):
        # fill this method and update the return
        for person in self._members:
            if person['id'] == id:
                return person
        return 'member does not exist'

    def get_member_name(self, name):
        # fill this method and update the return
        for person in self._members:
            if person['first_name'] == name:
                return person
        return 'member does not exist'

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        if len(self._members) > 0:
            return self._members
        else:
            return 'array is empty'
