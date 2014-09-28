docker stop `docker ps -q -a`
docker rm `docker ps -q -a`
docker run -d --name elastic-search -p 9200:9200 -p 9300:9300 pycon/elastic-search
docker run -d -p 80:5000  -v /vagrant:/application --link elastic-search:es pycon/search-app
