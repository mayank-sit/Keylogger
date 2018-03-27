#importing the autopy and time module of python
import autopy, time

#starting infinite loop
while (1):
	#ctime() output is in format 'Day Month Date Time Year'

    time_array = time.ctime().split(' ')	#Initializing an array and storing current time by splitting it using a white space.
	
    tstr = time_array[3].split(':')			#Storing time value in a variable as ctime() returns time in format xx:xx:xx.
	
    date = time_array[2]+'-'+time_array[1]+'-'+time_array[4]	#From array forming a proper date in DD-MMM-YYYY format.
	
    t = tstr[0]+'-'+tstr[1]+'-'+tstr[2]		#From tstr forming a proper time in xx-xx-xx format.
	
    time_string = date+'--'+t				#Appending date and time in a proper format as DD-MMM-YYYY--xx:xx:xx.
	
    bitmap = autopy.bitmap.capture_screen()	#Calling the capture_screen() function of bitmap module
	
    bitmap.save('C:\Screenshot\SS'+time_string+'.png')	#Saving the file at particular location.
	#Change loaction as per your convenience
	
    time.sleep(5)	#Sleep for 5 Seconds.
