import json
from pathlib import Path
from vulga_serializers.docx import get_collated_text

# if __name__ == "__main__":
#     vulga_report_path = Path('./tests/data/vulga_report.json')
#     vulga_report = vulga_report_path.read_text(encoding='utf-8')
#     vulga_report = json.loads(vulga_report)
#     output_dir = Path('./tests/data/')
#     text_title = "test"
#     collated_text = get_collated_text(vulga_report, output_dir, text_title)