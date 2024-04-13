import importlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from collections import OrderedDict

from colorama import Fore, Style

try:
    with open("preferences.json", "r") as f:
        preferences = json.load(f)
except FileNotFoundError:
    preferences = {"editor": "vim"}

try:
    with open("progress.json", "r") as f:
        user_progress = json.load(f)
except FileNotFoundError:
    user_progress = {}


def run_user_code(challenge_dir, input_value=""):
    solution_path = os.path.join(challenge_dir, "solution.py")
    test_case_path = os.path.join(challenge_dir, "test_cases.py")

    if os.path.exists(test_case_path):
        # Run unit tests for OOP challenges
        spec = importlib.util.spec_from_file_location("test_cases", test_case_path)
        test_cases_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_cases_module)

        suite = unittest.TestLoader().loadTestsFromModule(test_cases_module)
        runner = unittest.TextTestRunner(stream=sys.stdout)
        result = runner.run(suite)
        return result.wasSuccessful()
    else:
        # Run user code and check against expected outputs
        proc = subprocess.Popen(
            ["python", solution_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = proc.communicate(input=input_value)
        return stdout.strip(), stderr.strip()


class TestChallenge(unittest.TestCase):
    def test_challenges(self):
        challenges_dir = "challenges"
        chapters = OrderedDict()

        for chapter_name in os.listdir(challenges_dir):
            chapter_dir = os.path.join(challenges_dir, chapter_name)
            if os.path.isdir(chapter_dir):
                chapters[chapter_name] = OrderedDict()
                for challenge_name in os.listdir(chapter_dir):
                    challenge_dir = os.path.join(chapter_dir, challenge_name)
                    if os.path.isdir(challenge_dir):
                        with open(os.path.join(challenge_dir, "challenge.json"), "r") as f:
                            challenge = json.load(f)
                        difficulty_level = challenge.get("difficulty_level", "Intermediate")
                        chapters[chapter_name].setdefault(difficulty_level, []).append(challenge_name)

        while True:
            print("\nAvailable Chapters:")
            for i, chapter_name in enumerate(chapters.keys(), start=1):
                challenge_names = []
                for difficulty_level, names in chapters[chapter_name].items():
                    challenge_names.extend(names)
                solved_challenges = sum(1 for challenge_name in challenge_names if challenge_name in user_progress)
                total_challenges = len(challenge_names)
                progress_percentage = (solved_challenges / total_challenges) * 100 if total_challenges > 0 else 0
                print(f"{i}. {chapter_name} ({Fore.GREEN}{solved_challenges}/{total_challenges}{Style.RESET_ALL} - {progress_percentage:.2f}%)")

            choice = input("\nEnter the chapter number, 'e' to change editor, or 'q' to quit: ")

            if choice.lower() == 'q':
                break
            elif choice.lower() == 'e':
                editor_choice = input("Enter the editor command (e.g., 'vim', 'nano', 'code'): ")
                preferences["editor"] = editor_choice
                with open("preferences.json", "w") as f:
                    json.dump(preferences, f)
                print(f"Editor set to '{editor_choice}'")
                continue

            try:
                chapter_index = int(choice) - 1
                if 0 <= chapter_index < len(chapters):
                    chapter_name = list(chapters.keys())[chapter_index]
                    print(f"\nChapter: {chapter_name}")

                    challenge_dirs = chapters[chapter_name]
                    while True:
                        print("\nAvailable Challenges:")
                        for difficulty_level, challenge_names in challenge_dirs.items():
                            print(f"\n{difficulty_level}:")
                            for i, challenge_name in enumerate(challenge_names, start=1):
                                challenge_dir = os.path.join(challenges_dir, chapter_name, challenge_name)
                                status = (
                                    f"{Fore.GREEN}Solved{Style.RESET_ALL}"
                                    if challenge_name in user_progress
                                    else f"{Fore.RED}Unsolved{Style.RESET_ALL}"
                                )
                                print(f"{i}. {challenge_name} ({status})")

                        choice = input("\nEnter the challenge number or 'b' to go back: ")

                        if choice.lower() == 'b':
                            break

                        try:
                            challenge_index = int(choice) - 1
                            challenge_found = False
                            for difficulty_level, challenge_names in challenge_dirs.items():
                                if 0 <= challenge_index < len(challenge_names):
                                    challenge_name = challenge_names[challenge_index]
                                    challenge_dir = os.path.join(challenges_dir, chapter_name, challenge_name)
                                    if os.path.isdir(challenge_dir):
                                        with open(os.path.join(challenge_dir, "challenge.json"), "r") as f:
                                            challenge = json.load(f)

                                        print(f"\n{challenge['name']}")
                                        print(challenge["description"])

                                        if challenge_name in user_progress:
                                            print("You've already completed this challenge.")
                                            continue

                                        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
                                            temp_file_path = temp_file.name
                                            temp_file.write(challenge["description"])

                                        editor_command = preferences["editor"]
                                        os.system(f"{editor_command} -O {temp_file_path} {os.path.join(challenge_dir, 'solution.py')}")

                                        os.remove(temp_file_path)

                                        user_output = run_user_code(challenge_dir)

                                        if isinstance(user_output, bool):
                                            # OOP challenge with unit tests
                                            if user_output:
                                                print(f"{Fore.GREEN}All tests passed!{Style.RESET_ALL}")
                                            else:
                                                print(f"{Fore.RED}Some tests failed.{Style.RESET_ALL}")

                                            self.assertTrue(user_output)
                                        else:
                                            # Non-OOP challenge with expected outputs
                                            user_output, error = user_output
                                            if error:
                                                print(f"Error: {error}")
                                            else:
                                                for test_case in challenge["test_cases"]:
                                                    print(f"Input: {test_case['input']}")
                                                    print(f"Your Output: {user_output}")
                                                    print(f"Expected Output: {test_case['expected_output']}")
                                                    self.assertEqual(user_output, test_case["expected_output"])

                                        user_progress[challenge_name] = True
                                        with open("progress.json", "w") as f:
                                            json.dump(user_progress, f)

                                        challenge_found = True
                                        break

                            if not challenge_found:
                                print("Invalid choice. Please try again.")
                        except ValueError:
                            print("Invalid choice. Please try again.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    unittest.main()