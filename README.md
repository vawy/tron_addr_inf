# Get wallets info by address
микросервис, который выводит информацию по адресу в сети трон, его bandwidth, energy и баланс trx

1) склонируйте себе проект, например
```git clone git@github.com:vawy/tron_addr_inf.git```
2) после создайте в app/settings файл .env, куда поместите данные о бд
```bazaar
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=test_db
```
3) запустите
```bazaar
docker-compose up --build
```
