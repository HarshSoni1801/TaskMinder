# TaskMinder
#### Video Demo:  https://youtu.be/RvV7ax-FofE
#### Description:
TaskMinder is a Python-based project designed to help users manage their tasks and events efficiently. The core functionality of TaskMinder includes a to-do list and an event reminder system, which allows users to add, delete, and update tasks and events while receiving reminders for upcoming deadlines.

The project provides a simple yet powerful interface where users can input tasks or events, assign due dates, and track how much time remains until the deadline. TaskMinder then sorts tasks and events based on their proximity to the current date, making it easy for users to prioritize their to-dos.

### Key Features:
- **Task and Event Management**: Users can add tasks and events, set deadlines, and view the time left until those deadlines.
- **Emoji Integration**: The project uses emoji symbols to visually differentiate between completed tasks (✅) and incomplete tasks (❌), making it more interactive and user-friendly.
- **Deadline Tracking**: The project calculates the time remaining for tasks and events and displays this in days or hours, depending on the proximity of the deadline.
- **CSV File Support**: TaskMinder stores tasks and events in a CSV file, allowing users to maintain persistent data between sessions. The file stores information like task name, deadline, and completion status.

### Project Structure:
- **`taskminder.py`**: This file contains the main logic for the project, including functions for adding tasks, calculating time remaining, sorting events, and marking tasks as complete or incomplete.
- **`test_taskminder.py`**: A file with unit tests written in `pytest` to ensure the key functionality of TaskMinder works as expected. It tests functions like task addition, date formatting, and sorting tasks.
- **`README.md`**: The file you're currently reading. It provides a detailed description of the project, instructions for usage, and an overview of the file structure.
- **`tasks.csv`**: This CSV file stores all tasks and events, along with their deadlines and statuses. Every time the user adds, deletes, or completes a task, the file is updated.

### Design Choices:
Several design decisions were made during the development of TaskMinder:
1. **Sorting Tasks by Deadline**: This feature helps users to prioritize what’s due soon. I debated whether to sort by task priority or due date, but ultimately chose deadlines as the primary factor, as it's more intuitive for time management.
2. **Emoji Integration**: I initially considered using simple text labels for task statuses (like 'Completed' or 'Pending'), but decided that emojis would create a more engaging and visually appealing interface.
3. **Data Storage in CSV**: I chose to store data in a CSV file for simplicity and ease of use, as it is human-readable and allows for easy import/export without needing a database. Although using SQLite was considered, CSV offered a simpler approach for this project size.

### Future Improvements:
- Adding a graphical user interface (GUI) to make TaskMinder more accessible to non-technical users.
- Integrating notifications to alert users of upcoming deadlines, enhancing the reminder functionality.
- Allowing for task categorization, so users can sort tasks by type or priority, in addition to deadlines.

TaskMinder was developed as part of my journey in learning Python, and it incorporates various concepts such as file I/O, date manipulation, and unit testing. It’s a useful tool for managing daily tasks and events, and I plan to extend its functionality in the future.
