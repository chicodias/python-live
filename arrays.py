# 1. What is the length of the contacts list?

contacts = []
len(contacts)

# 2. Add the following people to the contacts list.

jake = {
    'name': 'Jake Overall',
    'email': 'jake.overall@boisecodeworks.com',
    'title': 'founder'
}

matt = {
    'name': 'Matt Overall',
    'email': 'matt.overall@boisecodeworks.com',
    'title': 'founder'
}

tony = {
    'name': 'Mark Ohnsman',
    'email': 'mark@boisecodeworks.com',
    'title': 'instructor'
}

andrew = {
    'name': 'Darryl Kilzer',
    'email': 'darryl@boisecodeworks.com',
    'title': 'instructor'
}

tom = {
    'name': 'Tom Day',
    'email': 'tom@boisecodeworks.com',
    'title': 'instructor'
}

contacts.extend([tom, andrew, tony, matt, jake])

# 3. Woops after adding all of those people to the same contacts list you realized you need a list just the instructors.
# create a new variable named instructors and populate it using the contacts list.
instructors = []

for contact in contacts:
    if contact['title'] == 'instructor':
        instructors.append(contact)
