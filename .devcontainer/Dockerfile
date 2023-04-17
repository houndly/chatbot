FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Configura el contenedor para usar bash en lugar de sh
RUN ln -sf /bin/bash /bin/sh

# Instala las dependencias de Python necesarias
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3 python3-pip python3-setuptools python3-wheel \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Establece el shell predeterminado
SHELL ["/bin/bash", "-c"]

# Establece el comando predeterminado para ejecutar en el contenedor (opcional)
CMD ["python", "main.py"]