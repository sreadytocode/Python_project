import pdb
from models.image import Image
from models.garment import Garment
from models.brand import Brand

import repositories.image_repository as image_repository
import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository

garment_repository.delete_all()
brand_repository.delete_all()
image_repository.delete_all()

brand1 = Brand("Asim Jofa")
brand_repository.save(brand1)

brand2 = Brand("Sana Safinaz")
brand_repository.save(brand2)

garment1 = Garment("Mint and gold dress", brand1, "Celestial mint and gold dress with embroidered chiffon and silk.", 15, 100.00, 165.00)
garment_repository.save(garment1)

garment2 = Garment("Coral pink shalwar kameez", brand2, "A classic silhouette with embellishments provides a beautiful coral-pink look.", 16, 95.00, 150.00)
garment_repository.save(garment2)

garment3 = Garment("Black and gold dress", brand1, "A dreamy noir dress with delicate embroidery details on chiffon. A mix of thread combined with golden zari and sequins weaves a magic to create this flawless heavenly design.", 16, 90.00, 120.00)
garment_repository.save(garment3)

garment4 = Garment("Organza yellow sharara", brand2, "A stunningly accentuated shirt with beautiful florals. With an off white sharara trousers", 25, 110.00, 200.00)
garment_repository.save(garment4)

brands = brand_repository.select_all()

image1 = Image("Mint-and-gold-dress.webp", garment1)
image_repository.save(image1)

image2 = Image("Coral-pink-shalwar-kameez.webp", garment2)
image_repository.save(image2)

image3 = Image("Black-and-gold-dress.webp", garment3)
image_repository.save(image3)

image4 = Image("Organza-yellow-sharara.webp", garment4)
image_repository.save(image4)

image5 = Image("")

breakpoint