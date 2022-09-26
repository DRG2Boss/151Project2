studentdata = open('Project2.txt', 'r')
sdata_lines = studentdata.readlines()
for lines in sdata_lines:
    sdata_seperated = lines.split(':')
    sid = sdata_seperated[0]
    sgpa = sdata_seperated[2]
    print(f"ID #{sid}, {sgpa}")
