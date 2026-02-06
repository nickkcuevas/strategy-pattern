Strategy Example In Python

So, first you need to run this:

$ virtualenv venv

$ source venv/bin/activate

Once you have your virtualenv up and running you will run:

$ pip install -r requirements.txt

Then, run the app $ python main.py

And start testing it with curl:

curl http://localhost:8000/api/formats


# JSON
curl "http://localhost:8000/api/data?format=json"

# XML
curl "http://localhost:8000/api/data?format=xml"

# CSV
curl "http://localhost:8000/api/data?format=csv"

# YAML
curl "http://localhost:8000/api/data?format=yaml"

# TOML
curl "http://localhost:8000/api/data?format=toml"