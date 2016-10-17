#! usr/bin/env python
import os,csv,sys
from time import strptime

def make_sipri_dict(siprifile,sipridir,sipridict):
    curdir=os.getcwd()
    os.chdir(sipridir)
    counter=0
    with open(siprifile,'rt') as sipri_input:
        reader=csv.reader(sipri_input)
        for row in reader:
            cname=row[0]
            ccode=row[1]
            if counter==0:
                if cname!='Country':
                    sys.exit("SIPRI err: first col should be 'Country'")
                if ccode!='ccode':
                    sys.exit("SIPRI err: second col should be 'ccode'")
                try:
                    yrlist=[int(i) for i in row[2:] if i]
                except ValueError:
                    sys.exit("SIPRI err: third col and beyond should be integer years")
                counter+=1
                continue
            try:
                ccode=int(row[1])
            except ValueError:
                counter+=1
                continue
            vallist=row[2:]
            if any('%' in val for val in vallist):
                vallist=[i.rstrip('%') for i in vallist if i]
            if len(vallist)!=len(yrlist):
                sys.exit("SIPRI err: are there blanks in your values?")
            for val in range(0,len(vallist)):
                sipri_tuple=(ccode,yrlist[val])
                sipridict[sipri_tuple]=vallist[val]
            counter+=1
    os.chdir(curdir)
    return sipridict

def cannedmonthnum(month_str):
    try:
        month_no=strptime(month_str,'%b').tm_mon
    except ValueError:
        try:
            month_no=strptime(month_str,'%B').tm_mon
        except ValueError:
            month_no=0
    return month_no

def date_dmy_check(cur_list_dmy,start_list_dmy,end_list_dmy,yrprefix=False):
    #REQUIRES a DMY. Just choose boundaries yourself if aggregating.
    sd=int(start_list_dmy[0])
    ed=int(end_list_dmy[0])
    cd=int(cur_list_dmy[0])
    sy=start_list_dmy[2]
    ey=end_list_dmy[2]
    cy=cur_list_dmy[2]
    try:
        sm=int(start_list_dmy[1])
    except ValueError:
        sm=cannedmonthnum(start_list_dmy[1])
        if sm==0:
            sm=input("input an integer for this month: "+str(start_list_dmy[1])+":_")
    sm=int(sm)
    try:
        em=int(end_list_dmy[1])
    except ValueError:
        em=cannedmonthnum(end_list_dmy[1])
        if em==0:
            em=input("input an integer for this month: "+str(end_list_dmy[1])+":_")
    em=int(em)
    try:
        cm=int(cur_list_dmy[1])
    except ValueError:
        cm=cannedmonthnum(cur_list_dmy[1])
        if cm==0:
            cm=input("input an integer for this month: "+str(cur_list_dmy[1])+":_")
    cm=int(cm)
    if len(str(sy))<4:
        if yrprefix==False:
            sy=input("input a year for this one: "+str(sy)+":_")
        else:
            sy=str(yrprefix)+str(sy)
        sy=int(sy)
    if len(str(ey))<4:
        if yrprefix==False:
            ey=input("input a year for this one: "+str(ey)+":_")
        else:
            ey=str(yrprefix)+str(ey)
        ey=int(ey)
    if len(str(cy))<4:
        if yrprefix==False:
            cy=input("input a year for this one: "+str(cy)+":_")
        else:
            cy=str(yrprefix)+str(ey)
        cy=int(cy)
    ret=1
    if cy<sy or cy>ey:
        ret=0
    elif cy==sy and cm<sm:
        ret=0
    elif cy==sy and cm==sm and cd<sd:
        ret=0
    elif cy==ey and cm>em:
        ret=0
    elif cy==ey and cm==em and cd>ed:
        ret=0
    return ret

def UCDPRegions(_ccode,regname=False):
    ########
    #Region information from
    #   "UCDP Armed Conflict Dataset Codebook"
    #       2016. v4-2016. page 13.
    #Region codes 1-5:
    ##Europe; ME; Asia; Af; Amer.
    ##(200-395); (630-698); (700-900); (400-626); (2-265)
    ###This includes South Sudan, ccode 626.
    #########
    try:
        if 2<=int(_ccode)<=165:
            _reg=5
            _rname="Americas"
        elif 200<=int(_ccode)<=395:
            _reg=1
            _rname="Europe"
        elif 400<=int(_ccode)<=626:
            _reg=4
            _rname="Africa"
        elif 630<=int(_ccode)<=698:
            _reg=2
            _rname="Middle East"
        elif 700<=int(_ccode)<=990:
            _reg=3
            _rname="Asia"
        else:
            sys.exit("Your region doesn't fall in bounds")

        if regname==False:
            return(_reg)
        else:
            _rfin=[_reg,_rname]
            return(_rfin)
    except ValueError:
        if regname==False:
            _reg="NA"
            return(_reg)
        else:
            _rfin=["NA","NA"]
            return(_rfin)
