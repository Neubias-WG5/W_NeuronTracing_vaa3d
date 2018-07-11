FROM neubiaswg5/neubias-base

ADD https://github.com/Vaa3D/release/releases/download/v3.458/Vaa3D_CentOS_64bit_v3.458.tar.gz /
RUN tar -xvzf Vaa3D_CentOS_64bit_v3.458.tar.gz

ADD wrapper.py /app/wrapper.py
ADD workflow.py /app/workflow.py

RUN apt-get install -y \
        libqt4-svg \
        libqt4-opengl \
        libqt4-network \
        libglu1-mesa
RUN apt-get install -y curl xvfb libx11-dev libxtst-dev libxrender-dev 


ENTRYPOINT ["python", "/app/wrapper.py"]


