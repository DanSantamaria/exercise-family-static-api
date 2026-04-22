"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = []
        self._next_id = 1

        # initial members
        self.add_member({"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]})
        self.add_member({"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]})
        self.add_member({"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]})

    # generate unique id
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        new_id = self._generateId()
        member["id"] = new_id
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, m in enumerate(self._members):
            if m["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def update_member(self, id, member_data):
        for member in self._members:
            if member["id"] == id:
                member["first_name"] = member_data.get("first_name", member["first_name"])
                member["age"] = member_data.get("age", member["age"])
                member["lucky_numbers"] = member_data.get("lucky_numbers", member["lucky_numbers"])
                return member
        return None

    def get_all_members(self):
        return self._members
