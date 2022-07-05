FROM amazoncorretto:11

RUN yum -y update \
    && yum install -y git wget tar zip which gcc python3 python3-dev python3-pip  \
    && yum install -y https://downloads.tableau.com/esdalt/2022.1.2/tableau-tabcmd-2022-1-2.noarch.rpm \
    && python3 -m ensurepip --default-pip \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install boto3 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

RUN /opt/tableau/tabcmd/bin/tabcmd --accepteula
