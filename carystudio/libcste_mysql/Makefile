# Created by: heimi
# $FreeBSD$

PORTNAME=	libcste_mysql
PORTVERSION=	0.9
PORTREVISION=	3
CATEGORIES=	www
MASTER_SITES=	http://esas.carystudio.com/temp/

MAINTAINER=	heimi_li@carystudio.com
COMMENT=	carystudio mysql function lib

INFO=		mysql function lib
BUILD_DEPENDS=  mysql:databases/mysql56-client
LIB_DEPENDS=	libcjson.so:carystudio/cjson

post-install:
	${INSTALL_LIB} ${WRKSRC}/libcste_mysql.so ${STAGEDIR}${PREFIX}/lib
	cp ${WRKSRC}/cste_mysql.h ${STAGEDIR}${PREFIX}/include/

.include <bsd.port.mk>
