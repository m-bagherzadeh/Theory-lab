import re

sample_text = """
sdfsdfsdfsdf+98-915-345-6789sdfsdf
09153456789
sdfsdfdsf00989153456789dsfsdff
1401/02/18 # date
24342341401/02/1934234234 # hidden date
24342dfgdfg341401/02/21342fdgdfg34234 # hidden date
"""

finds = re.findall(r'\d{4}/\d{2}/\d{2}', sample_text)
for find in finds:
    print(find)
