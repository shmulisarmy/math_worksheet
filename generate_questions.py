import sqlite3

connection = sqlite3.connect('scores.sqlite')
cursor = connection.cursor()

# Create the "people" table with the correct data types and default value
cursor.execute("""CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER, score INTEGER DEFAULT 0)""")

while True:
    age = int(input('age: '))
    name = input('name: ')

    # Use parameterized queries to prevent SQL injection
    cursor.execute("INSERT OR IGNORE INTO people (name, age) VALUES (?, ?)", (name, age))

    import random

    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    operator = random.choice(('+', '-'))
    result = n1 + n2 if operator == '+' else n1 - n2

    user_answer = int(input(f'\n{name}, what is {n1} {operator} {n2}: '))

    if user_answer == result:
        print("Correct!")
        # Use parameterized query to update the score
        cursor.execute("UPDATE people SET score = score + 1 WHERE name = ? AND age = ?", (name, age))
    else:
        print(f"Incorrect. The answer is {result}")
        cursor.execute("UPDATE people SET score = score - 1 WHERE name = ? AND age = ?", (name, age))

    # Execute the SELECT query and print the result
    cursor.execute("SELECT * FROM people")
    print(cursor.fetchone())

    connection.commit()

connection.close()
