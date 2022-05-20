import re

sample_text = """
sdfsdfsdfsdf+98-915-345-6789sdfsdf # hidden number
09153456789 # without a Country prefix
sdfsdfdsf00989153456789dsfsdff # hidden number
"""

finds = re.findall(r'\+98-\d{3}-345-\d{4}|00\d{12}', sample_text)
for find in finds:
    print(find)
