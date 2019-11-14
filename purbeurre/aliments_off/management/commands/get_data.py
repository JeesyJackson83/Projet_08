#! /usr/bin/env python3
# coding: utf-8

""" This script get data we need from OpenFoodfact """
from decimal import DecimalException
import requests
from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError
from aliments_off.models import Products


class Command(BaseCommand):
    help = 'Fill the database with products from pre-set categories'     

    def fill_db(self):        
        CATEGORIES = [
            "Aliments et boissons a base de vegetaux",
            "Aliments d'origine vegetale",
            "Snacks",
            "Boissons",
            "Snacks sucres",
            "Produits laitiers",
            "Viandes",
            "Plats prepares",
            "Boissons sans alcool",
            "Aliments a base de fruits et de legumes",
            "Cereales et pommes de terre",
            "Produits fermentes",
            "Produits a tartiner",
            "Biscuits et gateaux",
            "Desserts",
            "Boissons a base de vegetaux",
            "Produits a tartiner sucres",
            "Pates a tartiner vegetales",
            "Biscuits",
            "Chocolats",
            "Jus et nectars",
            "Yaourts",
            "Plats prepares a la viande",
        ]
        

        for category in CATEGORIES:

            research_url = 'https://fr.openfoodfacts.org/cgi/search.pl?tagtype_0=categories\
&tag_contains_0=contains&tag_0=%s&sort_by=unique_scans_n&page_size=500&action=process&json=1' \
                           % (category)
                
            r = requests.get(url=research_url)
            data_dict = r.json()
            products = data_dict['products']

            for product in products:
                try:
                    product_name = product["product_name_fr"]
                    id_product = product["code"]
                    nutritional_score = product["nutrition_grade_fr"]
                    url = product["url"]
                    img_url = product['image_front_url']
                    fat = product["nutrient_levels"]["fat"]
                    fat_100g = product["nutriments"]["fat_100g"]
                    saturated_fat = product["nutrient_levels"]["saturated-fat"]
                    saturated_fat_100g = product["nutriments"]["saturated-fat_100g"]
                    salt = product["nutrient_levels"]["salt"]
                    salt_100g = product["nutriments"]["salt_100g"]
                    sugars = product["nutrient_levels"]["sugars"]
                    sugars_100g = product["nutriments"]["sugars_100g"]

                    b = Products(
                        product_name=product_name, 
                        category_name=category, 
                        id_product=id_product, 
                        nutritional_score=nutritional_score, 
                        url=url, 
                        img_url=img_url, 
                        fat=fat,
                        fat_100g=fat_100g,
                        saturated_fat=saturated_fat,
                        saturated_fat_100g=saturated_fat_100g,
                        salt=salt,
                        salt_100g=salt_100g,
                        sugars=sugars,
                        sugars_100g=sugars_100g,
                        )
                    b.save()

                except DecimalException: 
                    pass

                except KeyError: 
                    pass

                except DataError:
                    pass

                except IntegrityError:
                    pass

    def handle(self, *args, **options):
        self.fill_db()
        self.stdout.write(self.style.SUCCESS("Base de données créée"), ending='')