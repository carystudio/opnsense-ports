# Created by: heimi
# $FreeBSD$

PORTNAME=	cste_heartbeat
PORTVERSION=	1.0
PORTREVISION=	3
CATEGORIES=	www
MASTER_SITES=	http://esas.carystudio.com/temp/

MAINTAINER=	heimi_li@carystudio.com
COMMENT=	carystudio mysql function lib

INFO=		mysql function lib
BUILD_DEPENDS=	mysql:databases/mysql56-client
LIB_DEPENDS=	libcste_mysql.so:carystudio/libcste_mysql
LIB_DEPENDS+=	libcjson.so:carystudio/cjson
LIB_DEPENDS+=	libsysinfo.so:devel/libsysinfo
LIB_DEPENDS+=	libcares.so:dns/c-ares

post-install:
	${INSTALL_PROGRAM} ${WRKSRC}/cste_heartbeat ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/cs_daemon.sh ${STAGEDIR}${PREFIX}/bin/cs_daemon.sh

.include <bsd.port.mk>
