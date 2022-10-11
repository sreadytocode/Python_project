from db.run_sql import run_sql

from models.garment import Garment
from models.brand import Brand
from models.type import Type
import repositories.brand_repository as brand_repository
import repositories.type_repository as type_repository

def save(garment):
    sql = """
    INSERT INTO garments(name, brand_id, type_id, description, stock_quantity, buying_cost, selling_price)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    RETURNING id
    """
    values = [garment.name, garment.brand.id, garment.type.id, garment.description, garment.stock_quantity, garment.buying_cost, garment.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    garment.id = id
    return garment

def select_all():
    garments = []

    sql = "SELECT * FROM garments"
    results = run_sql(sql)

    for row in results:
        brand = brand_repository.select(row['brand_id'])
        type = type_repository.select(row['type_id'])
        garment = Garment(row['name'], brand, type, row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        garments.append(garment)
    return garments

def select(id):
    garment = None
    sql = "SELECT * FROM garments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        brand = brand_repository.select(result['brand_id'])
        type = type_repository.select(result['type_id'])
        garment = Garment(result['name'], brand, type, result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], result['id'])
    return garment

def delete_all():
    sql = "DELETE FROM garments"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM garments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(garment):
    sql = """
    UPDATE garments SET 
    (name, brand_id, type_id, description, stock_quantity, buying_cost, selling_price)
    = (%s, %s, %s, %s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [garment.name, garment.brand.id, garment.type.id, garment.description, garment.stock_quantity, garment.buying_cost, garment.selling_price, garment.id]
    run_sql(sql, values)
