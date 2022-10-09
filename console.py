import pdb
from models.garment import Garment
from models.brand import Brand

import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository

garment_repository.delete_all()
brand_repository.delete_all()

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

brands = brand_repository.select_all()


breakpoint