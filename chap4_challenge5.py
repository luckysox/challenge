#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     11/11/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#----------------------------------------------------------------------------
def float_num(string):
    try:
        return float(string)
    except ValueError:
        print(少数型に変換できません)