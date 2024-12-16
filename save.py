import os

def save_hi_score(score : int):
    print("save")

    if not save_file_exists() or read_score() < score:
        print("save2")
        with open("savefiles/hi_score", 'w') as file:
            file.write(str(score))

def save_file_exists() -> bool:
    if not os.path.exists("savefiles"):
        os.mkdir("savefiles")

        with open("savefiles/hi_score", 'w') as file:
            pass

        return False
    
    return True

def read_score() -> int:
    if save_file_exists():
        with open("savefiles/hi_score") as file:
            score = 0
            line = file.readline()

            try:
                score = int(line)
            except ValueError:
                pass
        
        return score

    return 0