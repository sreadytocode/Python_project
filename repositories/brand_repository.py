from db.run_sql import run_sql

from models.garment import Garment
from models.brand import Brand

def save(brand):
    sql = """
    INSERT INTO brands (name, deactivate)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [brand.name, brand.deactivate]
    results = run_sql(sql, values)
    brand.id = results[0]['id']
    return brand

def select_all():
    brands = []

    sql = "SELECT * FROM brands order by name"
    results = run_sql(sql)

    for row in results:
        brand = Brand(row['name'], row['deactivate'], row['id'])
        brands.append(brand)
    return brands

def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        brand = Brand(result['name'], result['deactivate'], result['id'])
    return brand

def delete_all():
    sql = "DELETE FROM brands"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(brand):
    sql = """
    UPDATE brands SET (name, deactivate)
    = (%s, %s) 
    WHERE id = %s
    """
    values = [brand.name, brand.deactivate, brand.id]
    run_sql(sql, values)