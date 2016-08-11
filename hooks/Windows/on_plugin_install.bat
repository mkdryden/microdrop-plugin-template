REM Change into [parent directory of batch file][1].
REM
REM [1]: http://stackoverflow.com/questions/16623780/how-to-get-windows-batchs-parent-folder
REM Launch Microdrop
set PARENT_DIR=%~dp0
%1 "%PARENT_DIR..\..\on_plugin_install.py"
