# User Review Management Console Application

A simple terminal-based application for interacting with a user-review SQL database, featuring custom search functionality, social connection management, and review submission. Designed with a focus on usability, input validation, and flexible query options. Primary utilizes custom SQL queries for database interactions and modifications.

## Features:
- User Authentication
  - On startup, the system prompts for a User ID.
  - Validates the ID against the database before allowing access.
  - Prompts repeatedly until a valid ID is entered.

- Main Menu Options
  - Search for Businesses.
  - Search for Users.
  - Add a Friend.
  - Submit a Business Review.
  - Exit the Program.
(Input checking ensures the menu responds appropriately to invalid or unexpected entries. e.g., out-of-range numbers or alphabetic strings)

- Business Search
  - Businesses filter with the highest ratings.
  - Businesses filter with the lowest ratings.
  - Based on a specific city
  - Search by business name or a partial match.
(Results are displayed in alphabetical order by business name.)

- User Search
  - Search by name or partial name.
  - Users rated as useful.
  - Users known for being funny.
  - Users considered cool.
(Results are returned in name-sorted order.)

- Create Friendships
  - The system allows users to form social connections by entering another valid User ID.
  - Verifies if the provided ID exists before storing the relationship.
  - Confirms successful friendship creation in the database.

- Leave a Review
  - Users can select any valid business ID to leave a review.
  - Prompts re-entry if the business does not exist.
  - Confirms when the review is successfully saved.
 
## Design Principles
- Input Validation: Every user interaction is checked for correctness before proceeding.
- Flexible Filtering: Allows multi-criteria, out-of-order selection.
- Clear Feedback: Provides terminal output for all actions, including success and failure messages.
- Graceful Program Exit: The program only exits when the user explicitly chooses to quit.
