# ERD (Entity Relationship Diagram)

This diagram provides a high-level view of the relationships in the Dormitory Management System (Accommo).

```mermaid
erDiagram
    USERS ||--o{ ROOM_ASSIGNMENTS : has
    ROOMS ||--o{ ROOM_ASSIGNMENTS : "is assigned to"
    ROOMS }|--|| BUILDINGS : "belongs to"
    BUILDINGS ||--o{ ROOMS : has
    USERS ||--o{ PAYMENTS : makes
    ROOM_ASSIGNMENTS ||--o{ PAYMENTS : "associated with"
    REPORTS }o--|| USERS : generated_by
    BUILDINGS }|--o{ ROOM_TYPES : "(indirect)"
    USERS ||--o{ ROOM_INQUIRIES : makes
    ROOMS ||--o{ ROOM_INQUIRIES : receives
    USERS ||--o{ BUILDINGS : owns
    BUILDINGS }o--|| USERS : owned_by

    %% Legend
    %% USERS: (user_id) - role: admin, landlord, student
```

Notes:
- `BUILDINGS.owner_id` references `USERS.user_id` (Landlord)
- `ROOM_ASSIGNMENTS.user_id` references `USERS.user_id` (Tenant)
- `PAYMENTS.user_id` references `USERS.user_id` (Tenant)
- `PAYMENTS.recorded_by` references `USERS.user_id` (Admin)
- `REPORTS.generated_by` references `USERS.user_id` (Admin)
- `ROOM_INQUIRIES` ties students to rooms and optionally assigns landlord (owner of the building)

Use this as a quick ERD for the project. For a production diagram, use a graphical ERD tool.