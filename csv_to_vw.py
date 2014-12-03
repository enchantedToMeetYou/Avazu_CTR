# -*- coding: UTF-8 -*-

########################################################
# __Author__: Triskelion <info@mlwave.com>             #
# Kaggle competition "Display Advertising Challenge":  #
# http://www.kaggle.com/c/criteo-display-ad-challenge/ #
# Credit: Zygmunt ZajÄ…c <zygmunt@fastml.com>           #
########################################################

from datetime import datetime
from csv import DictReader

def csv_to_vw(loc_csv, loc_output, train=True):
	"""
	Munges a CSV file (loc_csv) to a VW file (loc_output). Set "train"
	to False when munging a test set.
	TODO: Too slow for a daily cron job. Try optimize, Pandas or Go.
	"""
	start = datetime.now()
	print("\nTurning %s into %s. Is_train_set? %s"%(loc_csv,loc_output,train))

	with open(loc_output,"wb") as outfile:
		for e, row in enumerate( DictReader(open(loc_csv)) ):
			categorical_features = ""
			numerical_features = ""
			for k,v in row.items():			
				if k == 'hour':
					hh = v[-2:]
					categorical_features += " %s" % hh
				elif k not in ['click','id']:
					categorical_features += " %s" % v
			#Create labels
			label = 1
			if train: #considering a training set
				if row['click'] == "1":
					label = 1
				else:
					label = -1
				outfile.write("%s '%s|c%s\n" % (label,row['id'],categorical_features) )
			else: #Test set
				outfile.write("-1 '%s|c%s\n" % (row['id'],categorical_features) )
			#Reporting progress, every million records
			if e % 1000000 == 0:
				print("%s\t%s"%(e, str(datetime.now() - start)))
				print("%s '%s|c%s\n" % (label,row['id'],categorical_features))
	print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))
