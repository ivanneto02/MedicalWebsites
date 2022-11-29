from dotenv import load_dotenv

import os

load_dotenv()

DATA_PATH = os.environ["DATA_PATH"]
DATA_NAME = os.environ["DATA_NAME"]
N_ROWS = int(os.environ["N_ROWS"])