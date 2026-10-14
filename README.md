
# Student Database Management System Using Hashing

## Aim
To implement a basic Student Database Management System using the Hashing technique in Python.

## Description
This project stores and searches student records using a Hash Table.

Each student record contains a roll number, name, and marks. A hash function calculates the index using the student's roll number.

Linear Probing is used to resolve collisions when two records map to the same index.

## Data Structure Used
- Hash Table
- Linear Probing for collision resolution

## Features
- Add a student record
- Search for a student by roll number
- Display all student records
- Handle duplicate roll numbers
- Handle hash collisions
- Validate student marks

## Technologies Used
- Python 3

## Hash Function
index = roll_number % table_size

## Collision Resolution
Linear Probing checks the next available table position when a collision occurs.

## How to Run
1. Install Python 3.
2. Save the code as `main.py`.
3. Open a terminal in the project folder.
4. Run:

   `python main.py`

## Time Complexity
- Insert: O(1) average, O(n) worst case
- Search: O(1) average, O(n) worst case
- Display: O(n)

Here, n is the hash table size.

## Limitation
Records are stored in memory and are lost when the program exits. This is an educational project, not a permanent database.

## Conclusion
This project demonstrates how hashing and linear probing can be used to store and retrieve student records efficiently.
