docker network create rede-app
docker run -d --name banco-redis --network rede-app redis:alpine
docker build -t app-python .
# estou rodando no macOS, por isso o 8080 ao invés do 5000
docker run -d --name web-app --network rede-app -p 8080:5000 -v $(pwd)/logs:/var/log/app app-python 
# caso não esteja usando o macOS:
# docker run -d --name web-app --network rede-app -p 5000:5000 -v $(pwd)/logs:/var/log/app app-python