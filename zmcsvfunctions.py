#! usr/bin/env python
import os,csv

def writerow(row,ofile,odir,aw):
	curdir=os.getcwd()
	os.chdir(odir)
	with open(ofile,aw) as output:
		writer=csv.writer(output)
		writer.writerow(row)
	os.chdir(curdir)


def normalize_row(row,lenorig):
	if len(row)<lenorig:
		diff=lenorig-len(row)
		for i in range(0,diff):
			row.append('')
	return row


def concat_csvs(csvfile_list,indir,csvoutname):
    if len(csvfile_list)>1:
        curdir=os.getcwd()
        os.chdir(indir)
        counter=0
        for file_ in csvfile_list:
            with open(file_,'rt') as f_:
                reader=csv.reader(f_)
                if counter>0:
                    reader.next()
                for row in reader:
                    if counter==0:
                        writerow(row,csvoutname,indir,'w')
                        counter+=1
                        continue
                    writerow(row,csvoutname,indir,'a')
                    counter+=1
        os.chdir(curdir)
        return csvoutname
    elif len(csvfile_list)==1:
        return csvfile_list[0]

def dict2csv(indict,ofile,odir,keyname='Key',valuename='Value'):
    #Treats dict values as a single entry, except
    #   for 1-D lists, which are added itemwise
    #   to the csv row.
    _header=[str(keyname),str(valuename)]
    curdir=os.getcwd()
    os.chdir(odir)
    with open(ofile,'w') as output:
        writer=csv.writer(output)
        writer.writerow(_header)
    
    for k,v in indict.items():
        _a=[k]
        if type(v)==list:
            for _i in v:
                _a.append(_i)
        with open(ofile,'a') as output2:
            writer=csv.writer(output2)
            writer.writerow(_a)
    os.chdir(curdir)