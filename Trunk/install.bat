@REM Install esm software 
@REM 
@REM File:      $URL$ 
@REM Version:   $Rev$ 
@REM Changed:   $Date$ 
@REM 
@REM Homepage:  http://esm.berlios.de 
@REM Copyright: GNU Public License Version 2 (see license.txt) 
@REM 
@REM E-Sportmanager (esm) 
@REM 
@REM Copyright (C) 2005 Jan Gottschick 
@REM 
@REM   This program is free software; you can redistribute it and/or modify it 
@REM   under the terms of the GNU General Public License as published by the 
@REM   Free Software Foundation; either version 2 of the License, or 
@REM   (at your option) any later version. 
@REM 
@REM   This program is distributed in the hope that it will be useful, but 
@REM   WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
@REM   or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
@REM   for more details. 
@REM 
@REM   You should have received a copy of the GNU General Public License along 
@REM   with this program; if not, write to the 
@REM 
@REM   Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 

@ECHO OFF 

PUSHD %~dp0%

SETLOCAL 

IF EXIST setenv.bat (
  @CALL setenv.bat
  nant -nologo -e -buildfile:esm.build install
) ELSE (
  ECHO :
  ECHO : !!!! Please run "setup.bat" first !!!!
  ECHO :
)

set /p WAIT=$ press return to finish 
ENDLOCAL 

POPD