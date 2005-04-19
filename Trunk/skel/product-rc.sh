#! /bin/sh
#
# File:      $URL$
# Version:   $Rev$
# Changed:   $Date$
#
# Homepage:  http://esm.berlios.de
# Copyright: GNU Public License Version 2 (see license.txt)
#
# E-Sportmanager (esm)
#
# Copyright (C) 2005 Jan Gottschick
#
#   This program is free software; you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#   or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#   for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the
#
#   Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
HOME=BASEDIR

NAME=@CONTEXT@
USER=esm

DAEMON=$HOME/$NAME/product-start
DDAEMON=$HOME/$NAME/product-debug

DESC="E-Sportmanager"

test -x $DAEMON || exit 0

set -e

case "$1" in
  start)
	echo -n "Starting $DESC: "
	start-stop-daemon --start --quiet --pidfile /var/run/$NAME.pid \
		-b -c $USER --exec $DAEMON
	echo "$NAME."
	;;
  debug)
	echo -n "Debugging $DESC: "
	$DDAEMON &
	echo "$NAME."
	;;
  stop)
	echo -n "Stopping $DESC: "
	start-stop-daemon --stop --quiet --pidfile $HOME/appserverpid.txt
	echo "$NAME."
	;;
  restart|force-reload)
	#
	#       If the "reload" option is implemented, move the "force-reload"
	#       option to the "reload" entry above. If not, "force-reload" is
	#       just the same as "restart".
	#
	echo -n "Restarting $DESC: "
	start-stop-daemon --stop --quiet --pidfile $HOME/appserverpid.txt
	sleep 1
	start-stop-daemon --start --quiet --pidfile /var/run/$NAME.pid \
		-b -c $USER --exec $DAEMON
	echo "$NAME."
	;;
  *)
	N=/etc/init.d/$NAME
	echo "Usage: $N {start|stop|restart|force-reload}" >&2
	exit 1
	;;
esac

exit 0
