from sqlalchemy import create_engine, text

conn_string = "postgresql://postgres.yuuololhrcglehfuyalc:s_K65dMhv_i993d@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"
engine = create_engine(conn_string)


def save_contact(contact_data):
    with engine.connect() as conn:
        query = text(
            "insert into users (name, phone, email) values (:name, :phone, :email)"
        )
        conn.execute(
            query,
            [
                {
                    "name": contact_data["name"],
                    "phone": contact_data["phone"],
                    "email": contact_data["email"],
                }
            ],
        )
        conn.commit()


def search(contact_data):
    with engine.connect() as conn:
        query = text("SELECT name, phone, email FROM users WHERE name = :name")
        result = conn.execute(
            query,
            [{"name": contact_data["name"]}],
        )
        contact = result.fetchone()
        if contact:
            return {"name": contact[0], "phone": contact[1], "email": contact[2]}
        else:
            return None


def delete(contact_data):
    with engine.connect() as conn:
        query = text(
            "DELETE FROM users WHERE name = :name AND phone = :phone AND email = :email"
        )
        conn.execute(
            query,
            {
                "name": contact_data["name"],
                "phone": contact_data["phone"],
                "email": contact_data["email"],
            },
        )
        conn.commit()


def show_all():
    with engine.connect() as conn:
        query = text("SELECT * FROM users")
        result = conn.execute(query)
        contact = result.fetchall()
        return contact
