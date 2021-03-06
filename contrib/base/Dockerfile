FROM debian:stretch
MAINTAINER Friedrich Lindenberg <friedrich@pudo.org>
ENV DEBIAN_FRONTEND noninteractive


# Enable non-free archive for `unrar`.
RUN echo "deb http://http.us.debian.org/debian stretch non-free" >/etc/apt/sources.list.d/nonfree.list
# Enable Node.js archive
RUN echo 'deb http://deb.nodesource.com/node_9.x stretch main' > /etc/apt/sources.list.d/nodesource.list
RUN apt-get update -y -q && apt-get install -y -q gnupg
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 68576280

RUN apt-get update -y -q && apt-get -y dist-upgrade && apt-get install -y -q  \
        curl git python-pip python-virtualenv build-essential python-dev \
        libxml2-dev libxslt1-dev libpq-dev apt-utils ca-certificates less \
        postgresql-client unrar unrar-free unzip locales libreoffice \
        libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev \
        liblcms2-dev poppler-utils poppler-data unrtf pstotext python-numpy \
        default-jdk libwebp-dev tcl8.6-dev tk8.6-dev python-tk python-pil \
        imagemagick-common imagemagick unoconv mdbtools \
        cabextract p7zip-full libboost-python-dev libgsf-1-dev \
        libtesseract-dev vim libicu-dev libldap2-dev libsasl2-dev \
        tesseract-ocr tesseract-ocr-all \
        nodejs djvulibre-bin \
    && apt-get -y autoremove && apt-get clean

RUN curl -s /tmp/pst.tgz http://www.five-ten-sg.com/libpst/packages/libpst-0.6.69.tar.gz > /tmp/pst.tgz \
    && cd /tmp && tar xvfz pst.tgz && cd libpst-0.6.69 && ln -s /usr/bin/python /usr/bin/python2.7.10 \
    && ./configure && make && make install

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# en_GB.UTF-8 UTF-8/en_GB.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# en_GB.ISO-8859-15 ISO-8859-15/en_GB.ISO-8859-15 ISO-8859-15/' /etc/locale.gen && \
    locale-gen
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

# WebKit HTML to X install since the one that comes with distros is hellishly outdated.
RUN curl -s -L https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz > /tmp/wkhtmltox.tar.xv \
    && tar -xf /tmp/wkhtmltox.tar.xv -C /opt && rm -f /tmp/wkhtmltox.tar.xv
ENV WKHTMLTOPDF_BIN /opt/wkhtmltox/bin/wkhtmltopdf
ENV TESSDATA_PREFIX /usr/share/tesseract-ocr

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
