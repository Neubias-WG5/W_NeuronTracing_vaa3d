FROM neubiaswg5/neubias-base

ADD https://github.com/Vaa3D/release/releases/download/v3.458/Vaa3D_CentOS_64bit_v3.458.tar.gz /
RUN tar -xvzf Vaa3D_CentOS_64bit_v3.458.tar.gz

ADD wrapper.py /app/wrapper.py
ADD workflow.py /app/workflow.py

