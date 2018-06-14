# Created by: heimi
# $FreeBSD$

PORTNAME=	cjson
PORTVERSION=	0.9
PORTREVISION=	3
CATEGORIES=	www
MASTER_SITES=	http://esas.carystudio.com/temp/

MAINTAINER=	heimi_li@carystudio.com
COMMENT=	port cjson lib

INFO=		cjson lib

post-install:
	${INSTALL_LIB} ${WRKSRC}/cjson.so ${STAGEDIR}${PREFIX}/lib/libcjson.so
	cp ${WRKSRC}/cJSON.h ${STAGEDIR}${PREFIX}/include/

.include <bsd.port.mk>
