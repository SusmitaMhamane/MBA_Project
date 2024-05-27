import sqlite3
from datetime import datetime

class DataCollector:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data
                               (timestamp TEXT, sensor_name TEXT, reading REAL)''')
        self.conn.commit()

    def collect_data(self, sensor):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        reading = sensor.get_reading()
        self.cursor.execute("INSERT INTO sensor_data VALUES (?, ?, ?)", (timestamp, sensor.name, reading))
        self.conn.commit()

# Usage:
collector = DataCollector('sensor_data.db')
temp_sensor = TemperatureSensor('temp_sensor')
collector.collect_data(temp_sensor)
