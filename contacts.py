contacts = {
    "number":4,
    "students":[
        {"name":"Sarah Holderness", "email":"sara@example.com"},
        {"name":"Harry Potter", "email":"harry@example.com"},
        {"name":"Hermione Granger", "email":"hermione@example.com"},
        {"name":"Ron Weasely", "email":"ron@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])