@echo off

rem Starting Hook program to hook keyboard.
start "" "F:\Python Programs\Hook.pyw"		

rem Starting Screenshot program to take screenshot(s).
start "" "F:\Python Programs\screenshot.pyw"	

rem Targeting a particular application ie., After launching Firefox it will start to hook each and every keypress.
start "" "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"	