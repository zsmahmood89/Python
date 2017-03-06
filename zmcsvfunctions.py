#! usr/bin/env python
import os,csv,sys

def writerow(row,ofile,odir,aw):
	curdir=os.getcwd()
	os.chdir(odir)
	with open(ofile,aw) as output:
		writer=csv.writer(output)
		writer.writerow(row)
	os.chdir(curdir)

def normalize_row(row,lenorig,pre=False):
    if len(row)<lenorig:
        diff=lenorig-len(row)
        for i in range(0,diff):
            if pre==False:
                row.append('')
            elif pre==True:
                row.insert(0,'')
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

def dict2csv(indict,ofile,odir,keyname='Key',valuename='Value',out_sort_key=False):
    #Maximum depth of keys and values is 1-dimension. For example,
    #(2011,482,2):[200,600] is written as row [2011,482,2,200,600].
    #If there's more depth, you'll just get that list as string in your row.
    #Note that lists and tuples are treated the same, in that
    #elements are written out itemwise.
    if type(keyname)==str:
        _keyhead=[keyname]
    elif type(keyname)==list:
        _keyhead=keyname
    else:
        sys.exit('for dict2csv, please pass a string or list for your key/val names')
    if type(valuename)==str:
        _valuehead=[valuename]
    elif type(valuename)==list:
        _valuehead=valuename
    else:
        sys.exit('for dict2csv, please pass a string or list for your key/val names')

    _header=_keyhead+_valuehead
    curdir=os.getcwd()
    os.chdir(odir)
    with open(ofile,'w') as output:
        writer=csv.writer(output)
        writer.writerow(_header)
    
    if out_sort_key==True and type(keyname)==list:
        sys.exit("dict2csv sorting functionality only available for single-key dictionaries")
    
    if out_sort_key==False:
        for k,v in indict.items():
            _a=[]
            if type(k)==list or type(k)==tuple:
                for _i in k:
                   _a.append(_i)
            else:
                _a.append(k)
            if type(v)==list or type(v)==tuple:
                for _i in v:
                    _a.append(_i)
            else:
                _a.append(v)

            with open(ofile,'a') as output2:
                writer=csv.writer(output2)
                writer.writerow(_a)

    elif out_sort_key==True:
        _araw=[]
        for k,v in indict.items():
            _tuplist=[]
            if type(k)==list or type(k)==tuple:
                sys.exit("dict2csv sorting functionality only available for single-key dictionaries")
            _tuplist.append(k)
            if type(v)==list or type(k)==tuple:
                for _i in v:
                    _tuplist.append(_i)
            else:
                _tuplist.append(v)

            _tup=tuple(_tuplist)
            _araw.append(_tup)
        _a=sorted(_araw,key=lambda x:x[0])
        for _tup in _a:
            _fin=list(_tup)
            with open(ofile,'a') as output2:
                writer=csv.writer(output2)
                writer.writerow(_fin)