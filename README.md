# 🎬 Django REST Framework - Cinema Reservation API

## 📌 Overview

This project is a complete practical implementation of **Django REST Framework (DRF)** concepts using a simple **Cinema Reservation System**.

The project demonstrates multiple ways to build APIs in Django REST Framework step by step, starting from normal Django responses until advanced DRF features such as:

- Function Based Views (FBV)
- Class Based Views (CBV)
- Mixins
- Generics
- ViewSets & Routers
- Authentication
- Permissions
- Pagination
- Token Authentication
- Custom Permissions

The project is organized as a learning roadmap across multiple days.

---

# 🚀 Technologies Used

- Python
- Django
- Django REST Framework (DRF)
- Token Authentication

---

# 📂 Models

The project contains the following models:

## 👤 User Model

Stores customer information.

Fields:

- `name`
- `mobile`

---

## 🎥 Movie Model

Stores movie details.

Fields:

- `movie`
- `hall`
- `date`

---

## 🎫 Reservation Model

Stores movie reservations.

Fields:

- `user`
- `movie`

---

## 📝 Post Model

Used later for authentication and permissions examples.

Fields:

- `title`
- `body`
- `author`

---

# 🔄 Serializers

The project includes the following serializers:

- `UserSerializers`
- `MoveSerializers`
- `ReservationSerializers`
- `PostSerializers`

These serializers handle:

- Model serialization
- Validation
- API data transformation

---

# 🌐 API Endpoints

---

# 1️⃣ No REST APIs

## ✅ No Model + No REST

| Method | URL                                      | Description                         |
| ------ | ---------------------------------------- | ----------------------------------- |
| GET    | `http://127.0.0.1:8000/no_rest_no_model` | Basic Django response without model |

---

## ✅ Model + No REST

| Method | URL                                        | Description                        |
| ------ | ------------------------------------------ | ---------------------------------- |
| GET    | `http://127.0.0.1:8000/no_rest_from_model` | Return data from model without DRF |

---

# 2️⃣ Function Based Views (FBV)

Using `@api_view` decorators.

## 📌 User APIs

### Get All Users

| Method | URL                              |
| ------ | -------------------------------- |
| GET    | `http://127.0.0.1:8000/fbv_user` |

Features:

- Pagination support

---

### Create New User

| Method | URL                              |
| ------ | -------------------------------- |
| POST   | `http://127.0.0.1:8000/fbv_user` |

Validation:

- Serializer validation enabled

Example Body:

```json
{
  "reservation": [],
  "name": "youssef",
  "mobile": "012"
}
```

---

## 📌 User By ID

### Get User

| Method | URL                                   |
| ------ | ------------------------------------- |
| GET    | `http://127.0.0.1:8000/fbv_user_id/7` |

---

### Update User

| Method | URL                                   |
| ------ | ------------------------------------- |
| PUT    | `http://127.0.0.1:8000/fbv_user_id/7` |

Validation Enabled

Example Body:

```json
{
  "name": "CVC44V",
  "mobile": "1234556656"
}
```

---

### Delete User

| Method | URL                                   |
| ------ | ------------------------------------- |
| DELETE | `http://127.0.0.1:8000/fbv_user_id/7` |

---

# 3️⃣ Class Based Views (CBV)

Using `APIView`.

## 📌 User APIs

### Get All Users

| Method | URL                               |
| ------ | --------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_cbv/` |

---

### Create User

| Method | URL                               |
| ------ | --------------------------------- |
| POST   | `http://127.0.0.1:8000/rest_cbv/` |

Validation Enabled

Example Body:

```json
{
  "name": "CVC44V",
  "mobile": "1234556656"
}
```

---

## 📌 User By ID

### Get User

| Method | URL                                 |
| ------ | ----------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_cbv/12` |

---

### Update User

| Method | URL                                 |
| ------ | ----------------------------------- |
| PUT    | `http://127.0.0.1:8000/rest_cbv/12` |

Example Body:

```json
{
  "name": "CVCV23",
  "mobile": "333333333333333333"
}
```

---

### Delete User

| Method | URL                                 |
| ------ | ----------------------------------- |
| DELETE | `http://127.0.0.1:8000/rest_cbv/12` |

---

# 4️⃣ Mixins + Generics

Using:

- `mixins`
- `GenericAPIView`

## 📌 APIs

### List + Create

| Method | URL                                  |
| ------ | ------------------------------------ |
| GET    | `http://127.0.0.1:8000/rest_mixins/` |
| POST   | `http://127.0.0.1:8000/rest_mixins/` |

Pagination:

- Enabled

Validation:

- Enabled

Example:

```json
{
  "name": "DSDS",
  "mobile": "54545422545"
}
```

---

## 📌 By ID

| Method | URL                                    |
| ------ | -------------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_mixins/15` |
| PUT    | `http://127.0.0.1:8000/rest_mixins/15` |
| DELETE | `http://127.0.0.1:8000/rest_mixins/15` |

---

# 5️⃣ Generics

Using DRF Generic Views.

## 📌 APIs

### List + Create

| Method | URL                                    |
| ------ | -------------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_generics/` |
| POST   | `http://127.0.0.1:8000/rest_generics/` |

Pagination:

- Enabled

Validation:

- Enabled

Example:

```json
{
  "name": "DrrSDwS",
  "mobile": "01255520633"
}
```

---

## 📌 By ID

| Method | URL                                      |
| ------ | ---------------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_generics/16` |
| PUT    | `http://127.0.0.1:8000/rest_generics/16` |
| DELETE | `http://127.0.0.1:8000/rest_generics/16` |

---

# 6️⃣ ViewSets & Routers

Using:

- `ModelViewSet`
- `Routers`

---

# 👤 User APIs

| Method | URL                                            |
| ------ | ---------------------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_viewsets/user/`    |
| POST   | `http://127.0.0.1:8000/rest_viewsets/user/`    |
| GET    | `http://127.0.0.1:8000/rest_viewsets/user/18/` |
| PUT    | `http://127.0.0.1:8000/rest_viewsets/user/18/` |
| DELETE | `http://127.0.0.1:8000/rest_viewsets/user/18/` |

Example:

```json
{
  "name": "DrrSDwS",
  "mobile": "01255520633"
}
```

---

# 🎥 Movie APIs

| Method | URL                                            |
| ------ | ---------------------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_viewsets/movie/`   |
| POST   | `http://127.0.0.1:8000/rest_viewsets/movie/`   |
| GET    | `http://127.0.0.1:8000/rest_viewsets/movie/2/` |
| PUT    | `http://127.0.0.1:8000/rest_viewsets/movie/3/` |
| DELETE | `http://127.0.0.1:8000/rest_viewsets/movie/3/` |

Example:

```json
{
  "movie": "nare 2",
  "hall": "a1",
  "date": "2024-01-14"
}
```

---

# 🎫 Reservation APIs

| Method    | URL                                                  |
| --------- | ---------------------------------------------------- |
| GET       | `http://127.0.0.1:8000/rest_viewsets/reservation/`   |
| POST      | `http://127.0.0.1:8000/rest_viewsets/reservation/`   |
| GET       | `http://127.0.0.1:8000/rest_viewsets/reservation/2/` |
| PUT/PATCH | `http://127.0.0.1:8000/rest_viewsets/reservation/2/` |
| DELETE    | `http://127.0.0.1:8000/rest_viewsets/reservation/1/` |

Example:

```json
{
  "user": 2,
  "movie": 2
}
```

---

# 🔍 Custom APIs

## 🎥 Find Movie

| Method | URL                                |
| ------ | ---------------------------------- |
| GET    | `http://127.0.0.1:8000/find_movie` |

Example:

```json
{
  "movie": "nare"
}
```

---

## 🎫 New Reservation

Create reservation with new user.

| Method | URL                                     |
| ------ | --------------------------------------- |
| POST   | `http://127.0.0.1:8000/new_reservation` |

Example:

```json
{
  "movie": "nare",
  "hall": "A2",
  "name": "XXXX4",
  "mobile": "01012369445"
}
```

---

# 🔐 Authentication

## Token Authentication

### Get Token / Login

| Method | URL                                     |
| ------ | --------------------------------------- |
| POST   | `http://127.0.0.1:8000/api-token-auth/` |

Example:

```json
{
  "username": "admin",
  "password": "adminadmin"
}
```

---

## Access Protected API

Headers:

```http
Authorization: Token abd5499e82f825f6337e7f47552ab9378ac9b92c
```

Example:

| Method | URL                              |
| ------ | -------------------------------- |
| GET    | `http://127.0.0.1:8000/fbv_user` |

---

# 🛡 Permissions

Custom Permission:

```python
IsAuthorOrReadOnly
```

Rules:

- Anyone can:

  - GET
  - CREATE

- Only Author can:

  - UPDATE
  - DELETE

---

# 📝 Posts APIs

## Get Posts

| Method | URL                                         |
| ------ | ------------------------------------------- |
| GET    | `http://127.0.0.1:8000/rest_post_generics/` |

---

## Create Post

| Method | URL                                         |
| ------ | ------------------------------------------- |
| POST   | `http://127.0.0.1:8000/rest_post_generics/` |

Example:

```json
{
  "title": "welcome admin",
  "body": "mmmmmm"
}
```

---

## Update Post

| Method | URL                                          |
| ------ | -------------------------------------------- |
| PUT    | `http://127.0.0.1:8000/rest_post_generics/3` |

Permission:

- Author only

---

## Delete Post

| Method | URL                                          |
| ------ | -------------------------------------------- |
| DELETE | `http://127.0.0.1:8000/rest_post_generics/3` |

Permission:

- Author only

---

# 🔑 Authentication Types

## Global Authentication

Configured inside:

```python
settings.py
```

Supported:

- `BasicAuthentication`
- `TokenAuthentication`

---

## Function-Level Authentication

Applied on:

- Function Based Views
- Class Based Views

---

# 📄 Pagination

Pagination enabled in:

- FBV
- Mixins
- Generics
- ViewSets

---

# 📚 Learning Roadmap

# ✅ Day 1

- Create Models:

  - User
  - Movie
  - Reservation

- Create Serializers:

  - MoveSerializers
  - UserSerializers
  - ReservationSerializers

- Create APIs:

  - no_rest_no_model
  - no_rest_from_model
  - fbv_user
  - fbv_user_id

---

# ✅ Day 2

Create APIs using:

- APIView
- Mixins

Endpoints:

- CBV_List
- CBV_pk
- mixins_list
- mixins_pk

---

# ✅ Day 3

Create APIs using:

- Generics
- ViewSets
- Routers

Endpoints:

- generics_list
- generics_pk
- viewsets_user

---

# ✅ Day 4

Added:

- BasicAuthentication
- TokenAuthentication
- Custom Permissions
- Post Model
- PostSerializers

---

# ▶️ Run Project

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

---

# 🎯 Project Goals

This project helps understand:

- Django REST Framework architecture
- API development styles
- Authentication & Permissions
- Serializer validation
- Pagination
- CRUD operations
- Token Authentication
- Routers & ViewSets
- Clean API structure

---

# 👨‍💻 Author

Developed for learning and practicing Django REST Framework concepts step by step.
