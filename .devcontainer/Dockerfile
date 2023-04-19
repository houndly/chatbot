FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Configura el contenedor para usar bash en lugar de sh
RUN ln -sf /bin/bash /bin/sh

# Instala las dependencias de Python necesarias
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok

RUN apt-get update && \
	apt-get -y install --no-install-recommends python3 python3-pip python3-setuptools python3-wheel
# autopep8 flask
# RUN mkdir -p /root/.ssh && \
#     chmod 0700 /root/.ssh && \
#     ssh-keygen -t rsa -b 4096 -C "jorgedevops20@gmail.com" -f /root/.ssh/id_rsa && \
#     eval $(ssh-agent -s) && \
#     ssh-add /root/.ssh/id_rsa

# Montar el directorio ~/.ssh del contenedor en un volumen
# VOLUME /root/.ssh

# Establece el shell predeterminado
SHELL ["/bin/bash", "-c"]

# Establece el comando predeterminado para ejecutar en el contenedor (opcional)
# CMD ["python", "main.py"]

