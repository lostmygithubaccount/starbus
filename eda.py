# imports
import os
import ibis
from dotenv import load_dotenv

# configure Ibis
ibis.options.interactive = True

# load env variables
load_dotenv()
user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# variables
host = "voda-sample.trino.galaxy.starburst.io"
port = 443
catalog = "sample"
schema = "demo"

# connect
con = ibis.trino.connect(
    user=user, password=password, host=host, port=port, database=catalog, schema=schema
)

astronauts = con.table("astronauts")
missions = con.table("missions")
