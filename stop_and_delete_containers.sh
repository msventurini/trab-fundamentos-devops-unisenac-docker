docker stop banco-redis || true
docker rm banco-redis || true
docker stop web-app || true
docker rm web-app || true
docker stop rede-app || true
docker rm rede-app || true