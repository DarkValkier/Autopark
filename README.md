# Autopark
###### Practical task for Yalantis Python School

Данный проект является практическим заданием для поступления в Yalantis Python School. Представляет из себя REST API сервис для парка машин с водителями.

Инструкция по разворачиванию проекта находится в файле [SETUP.md](SETUP.md).

База данных состоит из двух таблиц: Driver (водитель) и Vehicle (машина). Запросы, с которыми работает сервис:
> Обратите внимание, что вместо `UPDATE`-метода используется `PUT`-метод.
## Driver:
- **GET /drivers/driver/** - вывод списка водителей
- **GET /drivers/driver/?created_at__gte=10-11-2021** - вывод списка водителей, созданных после 10-11-2021
- **GET /drivers/driver/?created_at__lte=16-11-2021** - вывод списка водителей, созданных до 16-11-2021
- **GET /drivers/driver/<driver_id>/** - получение данных по конкретному водителю
- **POST /drivers/driver/** - создание нового водителя
- **PUT /drivers/driver/<driver_id>/** - изменение водителя
- **DELETE /drivers/driver/<driver_id>/** - удаление водителя

## Vehicle:
- **GET /vehicles/vehicle/** - вывод списка машин
- **GET /vehicles/vehicle/?with_drivers=yes** - вывод списка машин с водителями
- **GET /vehicles/vehicle/?with_drivers=no** - вывод списка машин без водителей
- **GET /vehicles/vehicle/<vehicle_id>** - получение информации по конкретной машине
- **POST /vehicles/vehicle/** - создание новой машины
- **PUT /vehicles/vehicle/<vehicle_id>/** - изменение машины
- **POST /vehicles/set_driver/<vehicle_id>/** - садим водителя в машину, высаживаем из машины  
- **DELETE /vehicles/vehicle/<vehicle_id>/** - удаление машины


## Формат передачи данных
Данные передаются посредством JSON. Пример ответа на GET-запрос:
```
{
  "status": "success",
  "data": [
    {
      "id": 6,
      "created_at": "15/12/2021 01:46:00",
      "updated_at": "15/12/2021 01:46:00",
      "first_name": "Николай",
      "last_name": "Ткаченко"
    }
  ]
}
```

При передаче данных через POST создавать объект "data" не нужно. Пример POST-запроса для водителя:
```
{
  "first_name": "Евгений",
  "last_name": "Дмитренко"
}
```
И для машины:
```
{
  "make": "ZIL",
  "model": "M3",
  "plate_number": "AA 4571 OO",
  "driver": 6
}
```

## Посадка водителя в машину

Для того, чтобы привязать водителя к машине, необходимо использовать запрос `POST /vehicles/set_driver/<vehicle_id>/`, указав вместо vehicle_id идентификатор машины, передав в запросе идентификатор водителя (или указав null):
```
{
  "driver": 1
}
```
