# Python Zero to Hero Challenge

This is a terminal-based Python challenge that guides you through various coding challenges from beginner to advanced level. The challenges are organized into chapters, and each chapter contains challenges sorted by difficulty level.

![ScreenCast](screen_cast.gif)

## Features

- Colorized output for solved and unsolved challenges
- Progress tracking for each chapter and overall progress
- Ability to change the default text editor
- Automatic testing of user solutions with test cases
  - Non-OOP challenges: Check against expected outputs
  - OOP challenges: Run unit tests defined in `test_cases.py`
- Persistent progress tracking across multiple sessions

## Prerequisites

- Python 3.x
- `colorama` library (install with `pip install colorama`)

## How to Run Locally

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Run the script with `python main.py`.
4. Follow the on-screen instructions to navigate through the chapters and challenges.

## How to Run with GitHub Codespaces

1. Navigate to the repository on GitHub.
2. Click on the "Code" button and select "Codespaces" from the dropdown menu.
3. Choose to create a new codespace or reuse an existing one.
4. Once the codespace is ready, open the terminal and run `python main.py`.
5. Follow the on-screen instructions to navigate through the chapters and challenges.

## Contributing

If you'd like to contribute to this project, you can:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

When contributing, please follow these guidelines:

- Follow the existing code style and formatting.
- Write clear and concise commit messages.
- Ensure that your changes don't break existing functionality by running the tests.
- If you're adding new features or making significant changes, update the documentation accordingly.

### Project Structure

The project has the following structure:

project_directory/
├── challenges/
│   ├── Chapter 1/
│   │   ├── challenge_1/
│   │   │   ├── challenge.json
│   │   │   └── solution.py
│   │   ├── challenge_2/
│   │   │   ├── challenge.json
│   │   │   └── solution.py
│   │   ├── ...
│   └── Chapter 2 - OOP/
│       ├── challenge_1/
│       │   ├── challenge.json
│       │   ├── solution.py
│       │   └── test_cases.py
│       ├── challenge_2/
│       │   ├── challenge.json
│       │   ├── solution.py
│       │   └── test_cases.py
│       └── ...
├── main.py
├── preferences.json
├── progress.json
└── requirements.txt


### Adding New Challenges

To add a new challenge, follow these steps:

1. Create a new directory for the challenge inside the appropriate chapter directory (e.g., `challenges/Chapter 1/challenge_3`).
2. Inside the challenge directory, create a `challenge.json` file and a `solution.py` file.
3. In the `challenge.json` file, define the challenge details, such as the name, description, difficulty level, and test cases (for non-OOP challenges).

Example `challenge.json` file:

```json
{
  "name": "Reverse String",
  "description": "Write a function that takes a string as input and returns the reverse of that string.",
  "difficulty_level": "Beginner",
  "test_cases": [
    {
      "input": "hello",
      "expected_output": "olleh"
    },
    {
      "input": "Python",
      "expected_output": "nohtyP"
    }
  ]
}