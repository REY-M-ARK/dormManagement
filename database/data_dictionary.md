# Data Dictionary (Accommo: Dormitory Management)

This data dictionary summarizes the primary tables and fields in the system.

## users
- user_id (PK) : int
- username : varchar(10)
- password_hash : varchar(255)
- role : varchar (admin|student|landlord)
- first_name, last_name : varchar
- email : varchar
- phone : varchar
- birth_date : date
- is_active : tinyint (1) - active
- created_at, updated_at : datetime

## buildings
- building_id (PK) : int
- building_name : varchar(100)
- address : varchar(255)
- total_floors : int
- owner_id (FK -> users.user_id) : int (optional landlord)
- is_active : tinyint(1)
- created_at, updated_at

## room_types
- type_id (PK)
- type_name : varchar(50)
- base_rate : decimal
- capacity : int
- description, features : text
- is_active, timestamps

## rooms
- room_id (PK)
- building_id (FK -> buildings)
- type_id (FK -> room_types)
- room_number : varchar
- floor_number : int
- is_available : tinyint(1)
- notes, timestamps

## room_assignments
- assignment_id (PK)
- user_id (FK -> users.user_id)
- room_id (FK -> rooms.room_id)
- start_date, end_date
- monthly_rate : decimal
- status : varchar (active, pending, cancelled)
- assigned_by : FK users.user_id
- notes, timestamps

## payments
- payment_id (PK)
- user_id (FK -> users.user_id)
- assignment_id (FK -> room_assignments)
- amount : decimal
- payment_method : varchar
- payment_date : date
- payment_period_start/payment_period_end : date
- receipt_number : unique
- recorded_by : FK users.user_id
- notes, timestamps

## reports
- report_id (PK)
- generated_by (FK -> users.user_id)
- report_type : varchar
- report_title : varchar
- file_path : varchar
- generated_on : datetime

## room_inquiries
- inquiry_id (PK)
- user_id (FK -> users.user_id) - the student that inquired
- room_id (FK -> rooms.room_id)
- landlord_id (FK -> users.user_id, optional) - landlord owner for the building
- message : text
- status : varchar (pending/approved/declined)
- processed_by : FK users.user_id
- created_at, updated_at


Notes:
- Primary keys are auto-incremented integers.
- Ensure appropriate indices for foreign keys for performance.
- Consider adding a new `building_owners` join table if multiple landlords can own a building.
- Timestamps can use DATETIME with default CURRENT_TIMESTAMP, and UPDATE triggers for updated_at.
