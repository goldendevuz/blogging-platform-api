# Blogging Platform API

This is an example API for a blogging platform using Django REST Framework.

## Endpoints

### 1. POST /posts/
Create a new post.
#### Request:
```json
{
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": 1,
  "tags": ["Tech", "Programming"]
}
```
#### Response:
```json
{
    "id": 1,
    "category": 1,
    "tags": [
        "Tech",
        "Programming"
    ],
    "created": "2025-03-01T14:43:24.108444+05:00",
    "modified": "2025-03-01T14:43:24.108593+05:00",
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post."
}
```

### 2. PATCH /posts/{id}/
Update an existing post.
#### Request:
```json
{
  "title": "My Updated Blog Post",
  "content": "This is the updated content of my first blog post."
}
```
#### Response:
```json
{
    "id": 1,
    "category": 1,
    "tags": [
        "Tech",
        "Programming"
    ],
    "created": "2025-03-01T14:43:24.108444+05:00",
    "modified": "2025-03-01T14:45:26.069765+05:00",
    "title": "My Updated Blog Post",
    "content": "This is the updated content of my first blog post."
}
```

### 3. GET /posts/{id}/
Retrieve a specific post.
#### Response:
```json
{
    "id": 1,
    "category": 1,
    "tags": [
        "Tech",
        "Programming"
    ],
    "created": "2025-03-01T14:43:24.108444+05:00",
    "modified": "2025-03-01T14:45:26.069765+05:00",
    "title": "My Updated Blog Post",
    "content": "This is the updated content of my first blog post."
}
```

### 4. GET /posts/
List all posts.
#### Response:
```json
[
    {
        "id": 1,
        "category": 1,
        "tags": [
            "Tech",
            "Programming"
        ],
        "created": "2025-03-01T14:43:24.108444+05:00",
        "modified": "2025-03-01T14:45:26.069765+05:00",
        "title": "My Updated Blog Post",
        "content": "This is the updated content of my first blog post."
    },
    {
        "id": 2,
        "title": "My Second Blog Post",
        "content": "This is the content of my second blog post.",
        "category": "Technology",
        "tags": ["Tech", "Programming"],
        "createdAt": "2021-09-01T12:30:00Z",
        "updatedAt": "2021-09-01T12:30:00Z"
    }
]
```

### 5. DELETE /posts/{id}/
Delete a specific post.

### 6. GET /posts?term=second
Search for posts containing a term.
#### Response:
```json
[
  {
    "id": 2,
    "tags": [
      "Tech",
      "Programming"
    ],
    "created": "2024-10-05T15:41:07.708386+05:00",
    "modified": "2024-10-05T15:41:07.708468+05:00",
    "title": "My Second Blog Post",
    "content": "This is the content of my second blog post.",
    "category": 1
  }
]
```

<details>
  <summary>Click me</summary>
  
  ## Other endpoints

### 1. POST /categories/
Create a new category.
#### Request:
```json
{
  "title": "Technology"
}
```
#### Response:
```json
{
    "id": 1,
    "created": "2025-03-01T14:39:31.655855+05:00",
    "modified": "2025-03-01T14:39:31.656029+05:00",
    "title": "Technology"
}
```

### 2. POST /posts/
Create a second post.
#### Request:
```json
{
  "title": "My Second Blog Post",
  "content": "This is the content of my second blog post.",
  "category": 1,
  "tags": ["Tech", "Programming"]
}
```
#### Response:
```json
{
    "id": 2,
    "category": 1,
    "tags": [
        "Tech",
        "Programming"
    ],
    "created": "2024-10-05T15:41:07.708386+05:00",
    "modified": "2024-10-05T15:41:07.708468+05:00",
    "title": "My Second Blog Post",
    "content": "This is the content of my second blog post."
}
```
</details>