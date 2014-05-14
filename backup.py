#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Backup files - for Automatically backup file with cron job
# by Seltenet Inc. 
# Credit: Rehmetjan Tursun, Yasin Abla

import sys, os, time

BAKFOLDER = 'E:\\backup_folder\\backup'
SRCFOLDER = 'E:\\projectx\\src'

""" Directory back up function. """
targetBackup = BAKFOLDER + time.strftime('%Y%m%d%H%M%S') + '.rar'

rar_command = "winrar a -r {0} {1}".format(targetBackup, SRCFOLDER)

if os.system(rar_command) == 0:
    print 'Successful backup to', targetBackup
else:
    print 'Backup FAILED'
    print BAKFOLDER
    print SRCFOLDER

