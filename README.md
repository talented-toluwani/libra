Libra is a backend API for managing library operations — books, authors, members, and loans — built with Django and Django REST Framework.

The system supports two roles: librarians, who manage the catalog and view all loan activity, and members, who can browse books and manage their own loans. Book availability updates automatically through Django signals whenever a loan is created or returned, so the catalog's copy counts always reflect reality without manual bookkeeping in the view layer.

Libra was built as a rebuild of an earlier CLI-based library management system, re-implemented as a production-style REST API to apply Django architecture, serializers, permissions, middleware, signals, and query-optimized ORM usage in a real, end-to-end service.

consciously chose a single serializer over splitting list/detail, given the dataset size didn't justify the extra complexity. That's a legitimate engineering judgment call, not a shortcut you need to hide.

Extra features can be : a way of adding bulk import of books through csv files.