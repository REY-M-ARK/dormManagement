"""
Debug script to check login issues
Run this to verify your database and credentials
"""

import sqlite3
from werkzeug.security import check_password_hash

def debug_login():
    print("=" * 60)
    print("LOGIN DEBUG TOOL")
    print("=" * 60)
    
    # Connect to database
    try:
        conn = sqlite3.connect('database/manager.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("✓ Database connection successful")
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return
    
    # Check if users table exists
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if cursor.fetchone():
            print("✓ Users table exists")
        else:
            print("✗ Users table not found!")
            print("  Run: python -c \"from db import init_db; init_db()\"")
            return
    except Exception as e:
        print(f"✗ Error checking table: {e}")
        return
    
    # Count users
    try:
        cursor.execute("SELECT COUNT(*) as cnt FROM users")
        count = dict(cursor.fetchone())['cnt']
        print(f"✓ Found {count} users in database")
        
        if count == 0:
            print("  No users found! Run: python seed_data.py")
            return
    except Exception as e:
        print(f"✗ Error counting users: {e}")
        return
    
    # Show all users
    print("\n" + "=" * 60)
    print("ALL USERS IN DATABASE:")
    print("=" * 60)
    
    try:
        cursor.execute("""
            SELECT user_id, username, role, first_name, last_name, 
                   email, is_active, password_hash
            FROM users
            ORDER BY user_id
        """)
        users = [dict(row) for row in cursor.fetchall()]
        
        for user in users:
            status = "ACTIVE" if user['is_active'] else "INACTIVE"
            has_pwd = "YES" if user['password_hash'] else "NO"
            print(f"\nID: {user['user_id']}")
            print(f"  Username: {user['username']}")
            print(f"  Role: {user['role']}")
            print(f"  Name: {user['first_name']} {user['last_name']}")
            print(f"  Email: {user['email']}")
            print(f"  Status: {status}")
            print(f"  Has Password: {has_pwd}")
            
    except Exception as e:
        print(f"✗ Error fetching users: {e}")
        return
    
    # Test login
    print("\n" + "=" * 60)
    print("PASSWORD VERIFICATION TEST")
    print("=" * 60)
    
    test_credentials = [
        ('admin', 'admin123'),
        ('landlord1', 'landlord123'),
        ('student1', 'student123'),
    ]
    
    for username, password in test_credentials:
        try:
            cursor.execute(
                "SELECT user_id, username, password_hash, is_active FROM users WHERE username=?",
                (username,)
            )
            row = cursor.fetchone()
            
            if not row:
                print(f"✗ {username}: USER NOT FOUND")
                continue
            
            user = dict(row)
            
            if not user['is_active']:
                print(f"✗ {username}: ACCOUNT INACTIVE")
                continue
            
            if not user['password_hash']:
                print(f"✗ {username}: NO PASSWORD HASH")
                continue
            
            if check_password_hash(user['password_hash'], password):
                print(f"✓ {username}/{password}: LOGIN WORKS!")
            else:
                print(f"✗ {username}/{password}: PASSWORD INCORRECT")
                
        except Exception as e:
            print(f"✗ {username}: ERROR - {e}")
    
    print("\n" + "=" * 60)
    print("DEBUG COMPLETE")
    print("=" * 60)
    
    conn.close()

if __name__ == '__main__':
    debug_login()