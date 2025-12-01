# Migration: Add owner_id to buildings

This file documents the SQL changes made to introduce `owner_id` (links buildings to a landlord user) and ties role-based UI to DB.

1) Backup your database
   - Always make a copy of the database before applying schema changes.

2) Postgres / MySQL (MySQL example) - Add column and FK

```sql
ALTER TABLE buildings
  ADD COLUMN owner_id INT DEFAULT NULL,
  ADD KEY fk_buildings_owner (owner_id),
  ADD CONSTRAINT fk_buildings_owner FOREIGN KEY (owner_id) REFERENCES users(user_id) ON DELETE SET NULL;
```

3) If you already have data and want to set an owner for existing buildings (e.g. admin),

```sql
UPDATE buildings SET owner_id = 1; -- set to admin or a landlord account
```

4) Optionally set specific buildings to landlords (example):

```sql
UPDATE buildings SET owner_id = 3 WHERE building_id = 1;  -- set Dormitory A to landlord with id 3
```

5) Re-run the app and log in as user with role `landlord` to see the role-based UI.

Notes
- The application code (`app.py`) now filters buildings, rooms, assignments, and payments based on the current user's role and the building owner relationship.
- Admins see everything; landlords see only their own buildings and associated rooms/assignments/payments; students see only their own assignments/payments and available rooms.
