# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:37:09 2017

@author: takyon
"""

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
intab='abcdefghijklmnopqrstuvwxyz'
outtab='cdefghijklmnopqrstuvwxyzab'
tab=str.maketrans(intab,outtab)

print(raw.translate(tab))