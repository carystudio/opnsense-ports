# $FreeBSD$

PORTNAME=	pim6
PORTVERSION=	20061214
CATEGORIES=	net ipv6
MASTER_SITES=	SF/mcast-tools
PKGNAMESUFFIX=	-tools
DISTNAME=	mcast-tools-${PORTVERSION}

MAINTAINER=	hrs@FreeBSD.org
COMMENT=	IPv6 multicast tools

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/COPYING

USE_HARDENING=	pie:off

USES=		autoreconf
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	YACC=${YACC}

post-install:
	${INSTALL_DATA} ${WRKSRC}/mfc/mfc.conf.sample ${STAGEDIR}${PREFIX}/etc

.include <bsd.port.mk>
