# Libra — Library Management API

A Django REST Framework API for managing a library's books, members, and loans — with JWT auth, role-based permissions, and signal-driven inventory tracking.

Libra was built as a Module 3 (Django & DRF) deliverable, rebuilding an earlier CLI-based Library Management System as a full, production-style REST API — applying Django architecture, serializers, permissions, middleware, signals, and query-optimized ORM usage in a real, end-to-end service.

---

## Features

- Full CRUD for Books, Authors, and Loans
- JWT authentication — register, login, refresh
- Role-based permissions — Librarians manage the catalog; Members manage their own loans
- Signal-driven availability tracking — a book's available copy count updates automatically when a loan is created or returned
- Pagination and filtering on list endpoints
- Custom request-logging middleware
- Query-optimized Loan list endpoint (see [Query Optimization](#query-optimization) below)

---

## Tech Stack

- **Django** — web framework
- **Django REST Framework (DRF)** — API layer
- **djangorestframework-simplejwt** — JWT authentication
- **django-filter** — endpoint filtering
- **SQLite** — database (development)

---

## Project Structure

```
libra/
├── libra_project/       # Project config: settings, root urls, middleware
├── accounts/            # Custom user model, registration
├── catalog/             # Author & Book models, serializers, views, permissions
├── loans/               # Loan model, serializers, views, permissions, signals
├── manage.py
├── requirements.txt
└── README.md
```

Each app owns its own models, serializers, views, and (where relevant) permissions and signals — `accounts` handles identity only, `catalog` handles the book collection, and `loans` handles borrowing activity. This separation keeps migrations, permission logic, and business rules scoped to the concern they actually belong to.

---

## Setup

```bash
# Clone the repo
git clone https://github.com/<talented-toluwani>/libra.git
cd libra

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (for Django admin access)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## Authentication

Libra uses JWT (via `djangorestframework-simplejwt`) rather than session-based auth for the API itself.

| Action | Endpoint | Method |
|---|---|---|
| Register | `/api/accounts/` | POST |
| Log in (obtain token) | `/api/token/` | POST |
| Refresh token | `/api/token/refresh/` | POST |

**Registration** requires `username`, `email`, `password`, and `role` (`"librarian"` or `"member"`, defaults to `"member"` if omitted).

**Using the token:** attach the returned `access` token to every subsequent request as:
```
Authorization: Bearer <access_token>
```

Access tokens expire after 60 minutes; refresh tokens after 1 day. Use `/api/token/refresh/` to obtain a new access token without logging in again.

---

## API Endpoints

### Catalog

| Endpoint | Methods | Access |
|---|---|---|
| `/api/authors/` | GET, POST | Read: anyone · Write: librarians only |
| `/api/authors/<id>/` | GET, PUT, PATCH, DELETE | Read: anyone · Write: librarians only |
| `/api/books/` | GET, POST | Read: anyone · Write: librarians only |
| `/api/books/<id>/` | GET, PUT, PATCH, DELETE | Read: anyone · Write: librarians only |

Books support filtering:
- `/api/books/?author=<id>` — filter by author
- `/api/books/?available=true` — only books with available copies

### Loans

| Endpoint | Methods | Access |
|---|---|---|
| `/api/loans/` | GET, POST | Any authenticated user |
| `/api/loans/<id>/` | GET, PUT, PATCH | Owner of the loan, or a librarian |

---

## Permissions

Two custom permission classes enforce the role system:

- **`IsLibrarianOrReadOnly`** (`catalog/permissions.py`) — anyone can read the catalog; only users with `role == "librarian"` can create, update, or delete Books or Authors.
- **`IsOwnerOrLibrarian`** (`loans/permissions.py`) — a member can only retrieve or update their own loan; librarians can access any loan.

Registration is deliberately open to unauthenticated users (`AllowAny`), since it's the entry point for creating an account in the first place.

---

## Design Decisions

Two deliberate choices worth calling out, made with the project's scope and timeline in mind:

**ForeignKey over ManyToManyField for `Book.author`.** A book having exactly one author is a simplification of reality (co-authored books exist), but it keeps serializers, filtering, and query optimization straightforward throughout the project. `select_related()` — the optimization used on the Loan endpoint below — pairs naturally with this choice; a M2M relationship would have required `prefetch_related()` instead, a genuinely different tool for a different kind of relationship.

**`generics` views for Loans, `ModelViewSet` for Books/Authors.** Books and Authors need full, symmetrical CRUD, so a `ModelViewSet` registered with a `DefaultRouter` gives all five operations from one class. Loans, by contrast, deliberately don't expose a blanket delete (borrowing history shouldn't just disappear), so `ListCreateAPIView` and `RetrieveUpdateAPIView` were used instead — a narrower, more intentional set of operations than a ViewSet would default to.

---

---

## Known Simplifications

Documented deliberately, given the project's timeline:

- Loan ownership filtering is enforced at the object level (`IsOwnerOrLibrarian`) on retrieve/update, but the list endpoint (`/api/loans/`) currently returns all loans regardless of requester — a `get_queryset()` override filtering by `request.user` would be the next iteration for stricter list-level scoping.
- One `BookSerializer` is used for both list and detail views rather than splitting into separate list/detail serializers, given the dataset size doesn't currently justify the added complexity.

---

## Author

Built by Miracle (Toluwani) as a Module 3 (Django & DRF) SIWES deliverable.