import numpy as np
import os, shutil, sys
import config as cf
import math
import time
import heapq
import subprocess


def change():

	nomi = ['Basket', 'BQT', 'Cactus']

	sequenze = ['BasketballDrive_1920x1080_50.yuv', 'BQTerrace_1920x1080_60.yuv', 'Cactus_1920x1080_50.yuv']

	qp = ['22', '27', '32', '37']


	for i in range(0, len(sequenze)):
		print('Video = ' + sequenze[i])
		
		for c in range(0, len(qp)):
			
			#cambio qp
			with open('encoder_randomaccess_main.cfg', 'r') as file:
				filedata=file.readlines()
				filedata[41]=filedata[41].replace(qp[c-1], qp[c])
			with open('encoder_randomaccess_main.cfg', 'w') as file:
				file.writelines(filedata)
		
			print('Qp = ' + qp[c])
			
			#avvio codificatore
			subprocess.call(['sh', 'RUN_ENC_RA.sh'])
			time.sleep(1)
			
			#cambio nomi file
			arr = os.listdir('/home/tiziano/Scaricati/HM-16.5_MIF-Net/bin/')
			for s in range(0, len(arr)):
				if (arr[s] == 'rec.yuv'):
					os.rename('rec.yuv', 'rec_' + nomi[i] + '-' + qp[c] + '.yuv')
				if (arr[s] == 'rec_nof.yuv'):
					os.rename('rec_nof.yuv', 'nof_' + nomi[i] + '-' + qp[c] + '.yuv')	
				if (arr[s] == 'rec_enhanced.yuv'):
					os.remove('rec_enhanced.yuv')
				if (arr[s] == 'rec_enhanced_total.yuv'):
					os.remove('rec_enhanced_total.yuv')
		
		if (i < len(sequenze)-1):
		
			#cambio sequenza
			with open('encoder_yuv_source.cfg', 'r') as file:
				filedata = file.read()
				filedata = filedata.replace(sequenze[i], sequenze[i+1])
			with open('encoder_yuv_source.cfg', 'w') as file:
				file.write(filedata)
			
	return 0 


if __name__ == "__main__":
	a = change() 
			
