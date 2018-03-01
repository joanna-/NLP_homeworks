import os
import json


class DataManager:
    JUDGMENT_DATE_KEY = "judgmentDate"

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def get_judgment_year(self, json_content):
        return int(json_content[self.JUDGMENT_DATE_KEY][:4])

    def judgments_generator(self, year='all'):
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json') and filename.startswith('judgments'):
                with open(os.path.join(self.data_dir, filename), 'r', encoding="utf8") as content_file:
                    content = content_file.read()
                    parsed = json.loads(content)
                    for judgment in parsed["items"]:
                        if year != 'all' and year == self.get_judgment_year(judgment) or year == 'all':
                            yield judgment
