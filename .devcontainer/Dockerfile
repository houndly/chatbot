FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Configura el contenedor para usar bash en lugar de sh
RUN ln -sf /bin/bash /bin/sh

# Instala las dependencias de Python necesarias
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok

RUN apt-get update && \
	apt-get -y install --no-install-recommends python3 python3-pip python3-setuptools python3-wheel

# Establece el shell predeterminado
SHELL ["/bin/bash", "-c"]

# Establece el comando predeterminado para ejecutar en el contenedor (opcional)
# CMD ["python", "main.py"]

