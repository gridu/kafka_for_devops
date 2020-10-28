rm -rf venv driver-feed.zip driver-feed.csv speed-events.zip speed-events.csv
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
./kafka-dataset-generator.py
