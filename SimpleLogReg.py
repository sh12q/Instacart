#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Created on Wed Jun 14 21:39:43 2017
#@author: tux
#print ('echo')
# hbase <table, RowKey, Column Family, Column, timestamp> -> Value

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
#filelisting
#from subprocess import check_output

#import data
#order_products_train_df = pd.read_csv("../InstacartData/order_products__train.csv")
#order_products_prior_df = pd.read_csv("../InstacartData/order_products__prior.csv")
#orders_df = pd.read_csv("../InstacartData/orders.csv")
#products_df = pd.read_csv("../InstacartData/products.csv")
#aisles_df = pd.read_csv("../InstacartData/aisles.csv")
#departments_df = pd.read_csv("../InstacartData/departments.csv")


orders_df.head(5)
order_products_prior_df.head(5)
products_df.head(5)


cnt_srs = orders_df.eval_set.value_counts()
plt.figure(figsize=(12,8))
sns.barplot(cnt_srs.index, cnt_srs.values, alpha=0.8, color=color[1])
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Eval set type', fontsize=12)
plt.title('Count of rows in each dataset', fontsize=15)
plt.xticks(rotation='vertical')
plt.show()
