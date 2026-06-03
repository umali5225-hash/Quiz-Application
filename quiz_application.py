# ============================================================
#   PROJECT 2: Quiz Application
#   Author   : SkillInfyTech Internship
#   Description: A multiple-choice quiz game with score
#                tracking, timer, and randomized questions.
# ============================================================

import random
import time

# ── Question Bank ─────────────────────────────────────────────

QUESTIONS = [
    {
        "question": "What is the correct file extension for Python files?",
        "options":  ["A) .py", "B) .pt", "C) .pyt", "D) .python"],
        "answer":   "A",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options":  ["A) func", "B) define", "C) def", "D) function"],
        "answer":   "C",
    },
    {
        "question": "What does the `len()` function return?",
        "options":  ["A) Last element", "B) Length of object", "C) Data type", "D) Index"],
        "answer":   "B",
    },
    {
        "question": "Which data type is used to store True/False values?",
        "options":  ["A) int", "B) str", "C) bool", "D) float"],
        "answer":   "C",
    },
    {
        "question": "How do you start a comment in Python?",
        "options":  ["A) //", "B) /*", "C) --", "D) #"],
        "answer":   "D",
    },
    {
        "question": "Which method is used to add an element to a list?",
        "options":  ["A) add()", "B) push()", "C) append()", "D) insert_end()"],
        "answer":   "C",
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options":  ["A) 6", "B) 8", "C) 9", "D) 23"],
        "answer":   "B",
    },
    {
        "question": "Which loop is used when the number of iterations is unknown?",
        "options":  ["A) for loop", "B) do-while", "C) while loop", "D) repeat loop"],
        "answer":   "C",
    },
    {
        "question": "What does `type()` function do?",
        "options":  ["A) Converts type", "B) Returns data type", "C) Checks error", "D) None of these"],
        "answer":   "B",
    },
    {
        "question": "Which module is used to generate random numbers?",
        "options":  ["A) math", "B) os", "C) sys", "D) random"],
        "answer":   "D",
    },
]


# ── Display Helpers ───────────────────────────────────────────

def print_banner():
    print("\n" + "=" * 55)
    print("           🧠 Python Quiz Application")
    print("=" * 55)


def print_result(score, total, time_taken):
    print("\n" + "=" * 55)
    print("              📊 QUIZ RESULTS")
    print("=" * 55)
    print(f"  Total Questions : {total}")
    print(f"  Correct Answers : {score}")
    print(f"  Wrong Answers   : {total - score}")
    print(f"  Score           : {score}/{total} ({(score/total)*100:.1f}%)")
    print(f"  Time Taken      : {time_taken:.1f} seconds")
    print("-" * 55)

    percentage = (score / total) * 100
    if percentage == 100:
        print("  🏆 Perfect Score! Outstanding!")
    elif percentage >= 80:
        print("  🥇 Excellent! Great Job!")
    elif percentage >= 60:
        print("  🥈 Good! Keep Practicing!")
    elif percentage >= 40:
        print("  🥉 Average. Review the topics.")
    else:
        print("  📚 Keep studying. You'll do better next time!")
    print("=" * 55 + "\n")


# ── Quiz Logic ────────────────────────────────────────────────

def get_player_name():
    name = input("  Enter your name: ").strip()
    return name if name else "Player"


def choose_difficulty():
    print("\n  Select Difficulty:")
    print("    1. Easy   (5 questions)")
    print("    2. Medium (7 questions)")
    print("    3. Hard   (10 questions)")
    while True:
        choice = input("\n  Your choice (1/2/3): ").strip()
        if choice == "1": return 5
        if choice == "2": return 7
        if choice == "3": return 10
        print("  ⚠️  Invalid choice. Please enter 1, 2, or 3.")


def run_quiz(player_name, num_questions):
    questions = random.sample(QUESTIONS, num_questions)
    score = 0
    start_time = time.time()

    print(f"\n  Hello {player_name}! Get ready...\n")
    time.sleep(1)

    for i, q in enumerate(questions, 1):
        print(f"  Q{i}/{num_questions}: {q['question']}")
        for opt in q["options"]:
            print(f"        {opt}")

        while True:
            answer = input("\n  Your Answer (A/B/C/D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("  ⚠️  Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("  ✅ Correct!\n")
            score += 1
        else:
            correct_opt = next(o for o in q["options"] if o.startswith(q["answer"]))
            print(f"  ❌ Wrong! Correct answer: {correct_opt}\n")

        time.sleep(0.5)

    time_taken = time.time() - start_time
    print_result(score, num_questions, time_taken)
    return score


# ── Main ──────────────────────────────────────────────────────

def main():
    print_banner()
    print("\n  Welcome to the Python Quiz!")
    print("  Test your Python knowledge and earn a score.\n")

    while True:
        player_name   = get_player_name()
        num_questions = choose_difficulty()
        run_quiz(player_name, num_questions)

        again = input("  🔁 Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print(f"\n  Thanks for playing, {player_name}! Goodbye! 👋\n")
            break
        print("\n" + "-" * 55 + "\n")


if __name__ == "__main__":
    main()
