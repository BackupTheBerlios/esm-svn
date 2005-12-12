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
@REM

@ECHO OFF

SETLOCAL
CLS

SET _MAX_ERRORS=3

PUSHD %~dp0%

IF EXIST setenv.bat @CALL setenv.bat

echo : Installation of E-Sportmanager (c) 2004,2005
echo :
echo : before you continue please make sure that you installed the following software:
echo :
echo :   - MySQL Database 3.x or higher    (http://dev.mysql.com/downloads/)
echo :   - nant 0.85 or higher             (http://nant.sourceforge.net)
echo :   - Python 2.3.x or higher          (http://www.python.org)
echo :   - Webware 0.8.x or higher         (http://webware.sourceforge.net)
echo :   - CheetahTemplate                 (http://www.cheetahtemplate.org)
echo :   - Python docutils 0.3.7 or higher (http://docutils.sourceforge.net)
echo :   - MySQL-python 1.x or higher      (http://dev.mysql.com/downloads/)
echo :   - ReportLab pdf tools             (http://www.reportlab.org)
echo :   - eGenix.com mx BASE package      (http://www.egenix.com)
echo :
set /p WAIT=$ press return to continue
echo :

SET _ERRORS=0
:python
echo :
echo : Enter the full path to your Python installation,
echo : e.g. "%ProgramFiles%\Python"
IF DEFINED PYTHON_HOME echo : default value = %PYTHON_HOME%
echo :
set /p PYTHON_HOME=$ Python Home = 
if NOT EXIST "%PYTHON_HOME%\python.exe" goto nopython

SET _ERRORS=0
:webware
echo :
echo : Enter the full path to your Webware installation,
echo : e.g. "%ProgramFiles%\webware"
IF DEFINED WEBWARE_HOME echo : default value = %WEBWARE_HOME%
echo :
set /p WEBWARE_HOME=$ Webware Home = 
if NOT EXIST "%WEBWARE_HOME%\WebKit" goto nowebware

SET _ERRORS=0
:context
echo :
echo : Enter the short name for your installation,
echo : e.g. "my_sport_club"
IF DEFINED _CONTEXT echo : default value = %_CONTEXT%
echo :
set /p _CONTEXT=$ Installation Name = 
if "%_CONTEXT%" EQU "" goto nocontext

SET _ERRORS=0
:organisation
echo :
echo : Enter the full name of your club,
echo : e.g. "My Sport Club e.V."
IF NOT DEFINED _ORGANISATION set _ORGANISATION=%_CONTEXT%
IF DEFINED _ORGANISATION echo : default value = %_ORGANISATION%
echo :
set /p _ORGANISATION=$ Club Name = 
if "%_ORGANISATION%" EQU "" goto noorganisation

SET _ERRORS=0
:title
echo :
echo : Enter the title of your installation,
echo : e.g. "My Sport Club Management"
IF NOT DEFINED _TITLE set _TITLE=%_CONTEXT%
IF DEFINED _TITLE echo : default value = %_TITLE%
echo :
set /p _TITLE=$ Title = 
if "%_TITLE%" EQU "" goto notitle

SET _ERRORS=0
:site
echo :
echo : Enter the unique shortcut/site of your installation,
echo : e.g. "sc1"
IF NOT DEFINED _SITE set _SITE=%_CONTEXT%
IF DEFINED _SITE echo : default value = %_SITE%
echo :
set /p _SITE=$ Site = 
if "%_SITE%" EQU "" goto nosite

SET _ERRORS=0
:link
echo :
echo : Enter the link to the website of your organisation,
echo : e.g. "http://www.My-Sport-Club.us"
IF NOT DEFINED _LINK set _LINK=
IF DEFINED _LINK echo : default value = %_LINK%
echo :
set /p _LINK=$ Link = 
if "%_LINK%" EQU "" goto nolink

SET _ERRORS=0
:mail
echo :
echo : Enter the mail address of your support/information,
echo : e.g. "support@My-Sport-Club.us"
IF NOT DEFINED _MAIL set _MAIL=
IF DEFINED _MAIL echo : default value = %_MAIL%
echo :
set /p _MAIL=$ Mail = 
if "%_MAIL%" EQU "" goto nomail

SET _ERRORS=0
:home
echo :
echo : Enter the path for your installation,
echo : e.g. "%ProgramFiles%\esm"
IF NOT DEFINED _HOME set _HOME=%ProgramFiles%\esm%
IF DEFINED _HOME echo : default value = %_HOME%
echo :
set /p _HOME=$ Installation Path = 
if "%_HOME%" EQU "" goto nohome

SET _ERRORS=0
:password
echo :
echo : Enter the password for the 'manager' account,
echo : e.g. "very_secret"
IF NOT DEFINED _PASSWORD set _PASSWORD=%_CONTEXT%
IF DEFINED _PASSWORD echo : default value = %_PASSWORD%
echo :
set /p _PASSWORD=$ Manager Password = 
if "%_PASSWORD%" EQU "" goto nopassword

SET _ERRORS=0
:dbname
echo :
echo : Enter the name of the database,
echo : e.g. "esm_my_sport_club"
IF NOT DEFINED _DBNAME set _DBNAME=esm_%_CONTEXT%
IF DEFINED _DBNAME echo : default value = %_DBNAME%
echo :
set /p _DBNAME=$ Database Name = 
if "%_DBNAME%" EQU "" goto nodbname

SET _ERRORS=0
:dbuser
echo :
echo : Enter the name of the database user,
echo : e.g. "esm_my_sport_club"
IF NOT DEFINED _DBUSER set _DBUSER=esm_%_CONTEXT%
IF DEFINED _DBUSER echo : default value = %_DBUSER%
echo :
set /p _DBUSER=$ Database User = 
if "%_DBUSER%" EQU "" goto nodbuser

SET _ERRORS=0
:dbpassword
echo :
echo : Enter the password of the database user,
echo : e.g. "4_My_Secret&"
echo :
set /p _DBPASSWORD=$ Database Password = 
if "%_DBPASSWORD%" EQU "" goto nodbpassword

goto generate

:nopython
echo :
echo :ERROR: Did not found "%PYTHON_HOME%\python.exe"
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto python

:nowebware
echo :
echo :ERROR: Did not found "%WEBWARE_HOME%\WebKit"
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto webware

:nocontext
echo :
echo :ERROR: The name of the installation must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto context

:noorganisation
echo :
echo :ERROR: The full name of the sport club must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto organisation

:notitle
echo :
echo :ERROR: The title of the installation must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto title

:nosite
echo :
echo :ERROR: The unique shortcut for your organization/site must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto site

:nolink
echo :
echo :ERROR: The link to the website of your organization must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto link

:nomail
echo :
echo :ERROR: The mail address of your organization must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto mail

:nohome
echo :
echo :ERROR: The path for the installation must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto home

:nopassword
echo :
echo :ERROR: The password for the 'manager' account must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto password

:nodbname
echo :
echo :ERROR: The name of the database must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto dbname

:nodbuser
echo :
echo :ERROR: The name of the database user must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto dbuser

:nodbpassword
echo :
echo :ERROR: The password for the database user must be given
SET /A _ERRORS+=1
IF "%_ERRORS%" GTR "%_MAX_ERRORS%" GOTO end
goto dbpassword

:generate

@ECHO :
@ECHO #### Generate 'setenv.bat' ####
@ECHO @REM set environment for E-Sportmanager installation > setenv.bat
@ECHO @REM >> setenv.bat
@ECHO SET PYTHON_HOME=%PYTHON_HOME%>> setenv.bat
@ECHO SET WEBWARE_HOME=%WEBWARE_HOME%>> setenv.bat
@ECHO SET _CONTEXT=%_CONTEXT%>> setenv.bat
@ECHO SET _HOME=%_HOME%>> setenv.bat
@ECHO SET _TITLE=%_TITLE%>> setenv.bat
@ECHO SET _ORGANISATION=%_ORGANISATION%>> setenv.bat
@ECHO SET _PASSWORD=%_PASSWORD%>> setenv.bat
@ECHO SET _DBNAME=%_DBNAME%>> setenv.bat
@ECHO SET _DBUSER=%_DBUSER%>> setenv.bat
@ECHO SET _DBPASSWORD=%_DBPASSWORD%>> setenv.bat

:end

echo :
echo : The following parameters have been set:
echo :
echo : Python Home =       "%PYTHON_HOME%"
echo : Webware Home =      "%WEBWARE_HOME%"
echo : Installation Name = "%_CONTEXT%"
echo : Installation Path = "%_HOME%"
echo : Database Name =     "%_DBNAME%"
echo : Database User =     "%_DBUSER%"
echo : Database Password = "%_DBPASSWORD%"
echo :

echo :
set /p WAIT=$ press return to continue or N to cancel 

IF /I "%WAIT%" EQU "N" (
  ENDLOCAL
  POPD
) ELSE (
  ENDLOCAL
  POPD

  ECHO #### Start installation ####
  %~dp0%\install.bat
)
