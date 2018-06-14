# Created by: heimi
# $FreeBSD$

PORTNAME=	crpc
PORTVERSION=	18.5.12
PORTREVISION=	1
CATEGORIES=	www
MASTER_SITES=	http://esas.carystudio.com/temp/

MAINTAINER=	heimi_li@carystudio.com
COMMENT=	carystudio reverse proxy client 

INFO=		carystudio reverse proxy client
BUILD_DEPENDS=	

post-install:
	${INSTALL_PROGRAM} ${WRKSRC}/crpc ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
