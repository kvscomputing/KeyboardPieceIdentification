@echo off 
 for /R %%x in (*.bat) do (
 if not "%%x" == "%~0" call "%%x" 
)