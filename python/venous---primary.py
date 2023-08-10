# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"100103.0","system":"med"},{"code":"101733.0","system":"med"},{"code":"104342.0","system":"med"},{"code":"105403.0","system":"med"},{"code":"106482.0","system":"med"},{"code":"106850.0","system":"med"},{"code":"107851.0","system":"med"},{"code":"1224.0","system":"med"},{"code":"15382.0","system":"med"},{"code":"20161.0","system":"med"},{"code":"20676.0","system":"med"},{"code":"22006.0","system":"med"},{"code":"22038.0","system":"med"},{"code":"25478.0","system":"med"},{"code":"27284.0","system":"med"},{"code":"28309.0","system":"med"},{"code":"31390.0","system":"med"},{"code":"32002.0","system":"med"},{"code":"3392.0","system":"med"},{"code":"3576.0","system":"med"},{"code":"3585.0","system":"med"},{"code":"36568.0","system":"med"},{"code":"37947.0","system":"med"},{"code":"38099.0","system":"med"},{"code":"39344.0","system":"med"},{"code":"41180.0","system":"med"},{"code":"42506.0","system":"med"},{"code":"43555.0","system":"med"},{"code":"48920.0","system":"med"},{"code":"49715.0","system":"med"},{"code":"54205.0","system":"med"},{"code":"5503.0","system":"med"},{"code":"55661.0","system":"med"},{"code":"55883.0","system":"med"},{"code":"55885.0","system":"med"},{"code":"57100.0","system":"med"},{"code":"58023.0","system":"med"},{"code":"58166.0","system":"med"},{"code":"61366.0","system":"med"},{"code":"61760.0","system":"med"},{"code":"64467.0","system":"med"},{"code":"65855.0","system":"med"},{"code":"70455.0","system":"med"},{"code":"70467.0","system":"med"},{"code":"824.0","system":"med"},{"code":"84404.0","system":"med"},{"code":"8769.0","system":"med"},{"code":"91282.0","system":"med"},{"code":"94496.0","system":"med"},{"code":"95077.0","system":"med"},{"code":"97808.0","system":"med"},{"code":"97853.0","system":"med"},{"code":"98526.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('venous-thromboembolic-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["venous---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["venous---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["venous---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
