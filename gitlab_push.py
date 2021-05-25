import os

def push_to_git():
    message_commit = str(input("Git message :"))
    step_4 = "git add ."
    step_5 = f"git commit -m '{message_commit}'"
    setp_6 = "git push"

    all_step_packaging = [step_4, step_5, setp_6]

    for step in all_step_packaging: os.system(f"{step}")


if __name__ == "__main__":
    push_to_git()