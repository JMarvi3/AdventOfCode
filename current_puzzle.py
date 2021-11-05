from dotenv import load_dotenv
from aocd.models import Puzzle
import os
import __main__


def current_puzzle():
    load_dotenv()
    main = __main__.__file__
    year = os.path.split(os.path.dirname(main))[1]
    day = os.path.splitext(os.path.basename(main))[0]
    return Puzzle(int(year), int(day))
