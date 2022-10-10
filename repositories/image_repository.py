from db.run_sql import run_sql

from models.image import Image
from models.garment import Garment
from models.brand import Brand
import repositories.garment_repository as garment_repository

def save(image):
    sql = """
    INSERT INTO images(name, garment_id)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [image.name, image.garment.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    image.id = id
    return image

def select_all():
    images = []

    sql = "SELECT * FROM images"
    results = run_sql(sql)

    for row in results:
        garment = garment_repository.select(row['garment_id'])
        image = Image(row['name'], garment, row['id'])
        images.append(image)
    return images

def select(id):
    image = None
    sql = "SELECT * FROM images WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        garment = garment_repository.select(result['garment_id'])
        image = Image(result['name'], garment, result['id'])
    return image

def delete_all():
    sql = "DELETE FROM images"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM images WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(image):
    sql = """
    UPDATE images SET (name, garment_id)
    = (%s, %s) 
    WHERE id = %s
    """
    values = [image.name, image.garment.id, image.id]
    run_sql(sql, values)