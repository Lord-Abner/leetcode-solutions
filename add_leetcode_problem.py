import os
import sys
import datetime

# Define folder paths for each difficulty level.
# These folders will be created in your repository if they don't exist.
DIFFICULTY_FOLDERS = {
    "easy": "easy/",
    "medium": "medium/",
    "hard": "hard/"
}

# Function to create a new Java file for a LeetCode problem.
def create_problem_file(difficulty, problem_name, leetcode_url):
    if difficulty not in DIFFICULTY_FOLDERS:
        print("Error: Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")
        return
    
    # Create a valid filename by converting the problem name to lower case and replacing spaces with underscores.
    filename = problem_name.lower().replace(" ", "_") + ".java"
    file_path = os.path.join(DIFFICULTY_FOLDERS[difficulty], filename)

    # Ensure that the target directory exists; if not, create it.
    os.makedirs(DIFFICULTY_FOLDERS[difficulty], exist_ok=True)

    # Java solution template (using an f-string for dynamic content).
    java_code_template = f"""// Problem: {problem_name}
// Difficulty: {difficulty.capitalize()}
// Source: {leetcode_url}
// Date Solved: {datetime.date.today()}

public class {problem_name.replace(" ", "")} {{
    public static void main(String[] args) {{
        System.out.println("Solution for {problem_name} goes here.");
    }}
}}
"""
    # Write the template to the new Java file.
    with open(file_path, "w") as file:
        file.write(java_code_template)
    
    print(f"✅ Created new problem file: {file_path}")
    
    # Update the README file in the corresponding folder.
    update_readme(difficulty, problem_name, leetcode_url)

# Function to update (or create) a README file for the specified difficulty folder.
def update_readme(difficulty, problem_name, leetcode_url):
    readme_path = os.path.join(DIFFICULTY_FOLDERS[difficulty], "README.md")

    # If the README doesn't exist, create it with a header.
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as file:
            file.write(f"# {difficulty.capitalize()} LeetCode Problems\n\n")

    # Append the new problem entry to the README.
    with open(readme_path, "a") as file:
        file.write(f"- [{problem_name}]({leetcode_url}) - Solved on {datetime.date.today()}\n")

    print(f"📌 Updated README in {difficulty}/")

# Function to commit changes and push them to GitHub.
def push_to_github(problem_name):
    # These system commands assume that Git is configured correctly in your repository.
    os.system("git add .")
    os.system(f'git commit -m "Added solution: {problem_name}"')
    os.system("git push origin main")
    print("🚀 Changes pushed to GitHub!")

# Main execution block: checks for the proper number of arguments and calls functions accordingly.
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python add_leetcode_problem.py <difficulty> <problem_name> <leetcode_url>")
        sys.exit(1)

    difficulty = sys.argv[1].lower()
    problem_name = sys.argv[2]
    leetcode_url = sys.argv[3]

    create_problem_file(difficulty, problem_name, leetcode_url)
    push_to_github(problem_name)
