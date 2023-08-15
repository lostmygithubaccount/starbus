# imports
import os
import ibis
from dotenv import load_dotenv

# load env variables
load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWORD")

# variables
host = "voda-sample.trino.galaxy.starburst.io"
port = 443
catalog = "sample"
schema = "demo"

# connect
con = ibis.trino.connect(
    user=user, password=password, host=host, port=port, database=catalog
)
