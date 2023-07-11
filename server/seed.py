from random import randint, choice as rc
from sqlalchemy import insert, engine
from datetime import datetime
from faker import Faker
from app import app
from models import (
    db,
    User,
    Product,
    Category,
    Order,
    OrderItems,
    OrderStatus,
    Cart,
    CartItem,
    Payment,
#     Review,
#     Comment,
    Address,
#     Role
)
import pickle
import os
# import ipdb
import json
import ast
import csv

# fake = Faker()



def declare_categories():
    db.session.query(Category).delete()
    NewCategories = []
    merch = Category(
        name = "Merch"
    )
    beard = Category(
        name = "Beard"
    )
    body = Category(
        name = "Body"
    )
    face = Category(
        name = "Face"
    )
    hair = Category(
        name = "Hair"
    )
    hair_growth = Category(
        name = "Hair Growth"
    )
    NewCategories.extend([        
        merch, 
        beard, 
        body, 
        face, 
        hair, 
        hair_growth])
    db.session.add_all(NewCategories)
    db.session.commit()

def declare_products():
    db.session.query(Product).delete()
    
    BeigeJogger = Product(
        name = "BoldSkin Jogger Set",
        price = 89.99,
        quantity = 50,
        e_pitch = "A Cozy Slip-in Jogger made from recycled and ethically sourced cotton, that you will never want to take off. Oh did i mention it look's really good on you To?",
        description = "Created in a cruelty free environment and made from ethically and recycled sourced cotton and hemp. A stylish and conscious way to end the Fast Fashion Trend that is slowly killings our planet.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/Beige_Jogger/Frnt%20Beige%20Jogger.png",
        image_2 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/Beige_Jogger/Back_Beige_Jogger.png",
        background = None,
        application = None,
        ingredients = "Cotton & Hemp",
        storage = "Wash on slow, on cold and warm and please airdry",
        category_id = 1
    )
    SummerJogger = Product(
        name = "Bozy Summer Time Set",
        price = 69.99,
        quantity = 50,
        e_pitch = "Think Cozy, Cool and Stylish. Also lessen's your carbon footprint, Who doesn't love that?",
        description = "Created in a cruelty free environment and made from ethically and recycled sourced cotton and hemp, but for Summertime . A stylish and conscious way to end the Fast Fashion Trend that is slowly killings our planet.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
        image_2 = None,
        background = None,
        application = None,
        ingredients = "Cotton & Hemp",
        storage = "Wash on slow, on cold and warm and please airdry",
        category_id = 1
    )
    WhiteT = Product(
        name = "Bold White T-shirt",
        price =  29.99,
        quantity = 50,
        e_pitch = "Bold Way to seperate yourself and Be concious at the same time. Also does help that you look Amazing in it, our designer's said 'Your Welcome'. ",
        description = "Created in a cruelty free environment and made from ethically and recycled sourced cotton and hemp. A stylish and conscious way to end the Fast Fashion Trend that is slowly killing our planet.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/White_T/White_T_Front.png",
        image_2 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/White_T/White_T_Back.png",
        background = None,
        application = None,
        ingredients = "Cotton & Hemp",
        storage = "Wash on slow, on cold and warm and please airdry",
        category_id = 1
    )
    BlackT = Product(
        name = "Bold Black T-shirt",
        price = 27.99,
        quantity = 50,
        e_pitch = "Bold Way to seperate yourself and Be concious at the same time. Also does help that you look Amazing in it, our designer's said 'Your Welcome'.",
        description = "Created in a cruelty free environment and made from ethically and recycled sourced cotton and hemp. A stylish and conscious way to end the Fast Fashion Trend that is slowly killing our planet.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/Black_T/Black%20Front%20T.png",
        image_2 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/Black_T/Back%20of%20Black%20T.png",
        background = None,
        application = None,
        ingredients = "Cotton & Hemp",
        storage = "",
        category_id = 1
    )
    LightGreyT = Product(
        name = "Bold LightGrey T-shirt",
        price = 34.99,
        quantity = 50,
        e_pitch = "Bold Way to seperate yourself and Be concious at the same time. Also does help that you look Amazing in it, our designer's said 'Your Welcome'.",
        description = "Created in a cruelty free environment and made from ethically and recycled sourced cotton and hemp. A stylish and conscious way to end the Fast Fashion Trend that is slowly killing our planet.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/LightGrey_T/White_Layered_Front.png",
        image_2 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/LightGrey_T/White_Layered%20_Back.png",
        background = None,
        application = None,
        ingredients = "Cotton & Hemp",
        storage = "Wash on slow, on cold and warm and please airdry",
        category_id = 1
    )
    WavyCurlComb = Product(
        name = "Wavy Curl Comb ",
        price = 24.99,
        quantity = 50,
        e_pitch = "Imagine a looking at a person with gorgeous hair and they pull out this stylish comb and you can't stop staring because you don't know which looks better, now imagine your that person being stared at is you.",
        description = "Comb designed to help get those wavy curls mositurized, untangled and ready for events of all types.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/3a%20Brush/Black_WBrush.png",
        image_2 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/3a%20Brush/Zebra_WBrush.png",
        background = None,
        application = None,
        ingredients = "Contains Recylced Materials, Non-Carcengonic ink",
        storage = "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time",
        category_id = 1
    )
    TightCurlComb = Product(
        name = "Tight Curl Comb",
        price = 24.99,
        quantity = 50,
        e_pitch = "Think of a 3c comb that doesn't pull on your scalp and make you go to bed with a tender scalp and is ethically sourced.",
        description = "Comb designed to help mositurize and get threw those tight curls in a easy and painless way , untangled and ready for events of all types.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/3c%20comb%20/3C%20comb%20front%20of%20Brush.png",
        image_2 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/3c%20comb%20/3C%20comb%20back%20of%20Brush.png",
        background = None,
        application = None,
        ingredients = "Contains Recylced Materials, Non-Carcengonic ink",
        storage = "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time",
        category_id = 1
    )
    FineComb = Product(
        name = "'Fine' Comb",
        price = 8.99,
        quantity = 50,
        e_pitch = "Standard 'Fine' comb but ethucally sourced & ethically made. Do you now what your Fine comb is made from and the carbo footprint it create's? ",
        description = "Standard & Stylish 'Fine' Comb Conciously designed to get threw those tight curls in a easy and painless way. ",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
        image_2 = None,
        background = None,
        application = None,
        ingredients = "Contains Recylced Materials, Non-Carcengonic ink",
        storage = "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time.",
        category_id = 1
    )
    MediumComb = Product(
        name = "'Medium' Comb",
        price = 9.99,
        quantity = 50,
        e_pitch = "Standard 'Medium' comb but ethucally sourced & ethically made. Do you now what your Fine comb is made from and the carbo footprint it create's?",
        description = "Standard & Stylish 'Medium' Comb Conciously designed to get threw those tight curls in a easy and painless way.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
        image_2 = None,
        background = None,
        application = None,
        ingredients = "Contains Recylced Materials, Non-Carcengonic ink",
        storage = "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time.",
        category_id = 1
    )
    ThickComb = Product(
        name = "'Thick' Comb",
        price = 10.99,
        quantity = 50,
        e_pitch = "Standard 'Thick' comb but ethucally sourced & ethically made. Do you now what your Fine comb is made from and the carbo footprint it create's?",
        description = "Standard & Stylish 'Thick' Comb Conciously designed to get threw those tight curls in a easy and painless way.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
        image_2 = None,
        background = None,
        application = None,
        ingredients = "Contains Recylced Materials, Non-Carcengonic ink",
        storage = "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time.",
        category_id = 1
    )
    SoftBristleBrush = Product(
        name = "Bamboo 'Soft' Bristle Brushe",
        price = 24.99,
        quantity = 50,
        e_pitch = "Ethically Sourced, durable, sustainable, and pocketable high-quality 'Soft' bristle brush",
        description = "Made out of the strongest and sustainable Wood on the planet, Recylcled-Bamboo, Paired with thousands of Non-Cruelty, Boar-Bristle Brushes. Boar-bristle brushes are know for their exceptional smoothing and shine-enhancing abilities. Built to last and built to apply the last brushes needed on any wave style.",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/Brushes/Bristle",
        image_2 = None,
        background = None,
        application = None,
        ingredients = "Cleanly-sourced and Reused-Bamboo, Cruelty-free Boar-Bristle Brushes",
        storage = "Regularly clean bristles every 3 months w/ soap and water. Do not soak or leave wood in Water for long perids of Time",
        category_id = 1
    )
    HardBristleBrush = Product(
        name = "Bamboo 'Hard' Bristle Brush",
        price = 27.99,
        quantity = 50,
        e_pitch = "Ethically Sourced, durable, sustainable, and pocketable high-quality 'Hard' bristle brush",
        description = "Made out of the strongest and sustainable Wood on the planet, Recylcled-Bamboo, Paired with thousands of Non-Cruelty, Boar-Bristle Brushes. Boar-bristle brushes are know for their exceptional smoothing and shine-enhancing abilities. Built to to get those tough curl patterns in-line and to last. ",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
        image_2 = None,
        background = None,
        application = None,
        ingredients = "Cleanly-sourced and Reused-Bamboo, Cruelty-free Boar-Bristle Brushes",
        storage = "Regularly clean bristles every 3 months w/ soap and water. Do not soak or leave wood in Water for long perids of Time",
        category_id = 1
    )
    FeelGoodLotion = Product(
        name = "Smell Good Lotion",
        price = 19.99,
        quantity = 50,
        e_pitch = "Imagine a lotion that doesn't feel gunky on your skin and almost make's you forget to apply cologne because it smells THAT GOOD. ",
        description = "Made with all skin type's in mind, oily, coarse, soft, and sensitive. Apply across body and watch the magic happen as you skin get's a Deep hydration and and nourishment. Made with skin revitalization in mind. Fragrance and nourish your body with this curated whipped Smell Good lotion loaded with nearly 25% rich butters and restorative tropical oils and extracts. As men we have a tendency to get up and Go but after 1-3 application's of this butter, your partner and your skin will thank you and we highly expect you to become a returning customer!",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/Lotion/Feel_Good_Lotion.png",
        image_2 = None,
        background = None,
        application = "For best result when applied to damp skin.",
        ingredients = "Kalahari Melon oil, Sorrel oil, Baobab oil, Sunflower oil, Rice Bran oil, Coconut oil, Jojoba oil, Shea Butter, Mango butter, Fragrance",
        storage = "Store in a low humid, cool, and Dry Place",
        category_id = 3
    )
    
    Smell_good_deodorant = Product(
        name = "Smell Good Deodorant",
        price = 14.99,
        quantity = 50,
        e_pitch = "Made for all type's of men wether it's All day constructuion or desk work. Your partner will thank you, and your Mom will ask 'What are you wearing? Smells Good. Guaranteed'.",
        description = "Smell good and forget the things that make you stress with our Feel Good Deodorant made with sustainability in mind and 99% plastic free. Our high-performance formula is naturally derived, clean, vegan & dermatologist-tested—formulated without parabens, phthalates and silicones. Our nature-inspired scents are bold, fresh, memorable and created with upcycled ingredients and essential oils. ",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/Deodorant/Deodorant.png",
        image_2 = None,
        background = None,
        application = "Apply after Fresh out of shower to smell good for the longest possible time",
        ingredients = "Hemp, Coconut oil, Rosemary Extract, Arrowroot Powder, Shea Butter, Sunflower Seed Wax, Candelilla Wax, (Rosemary) Flower Extract, Soybean oil, Lavandin Oil, Basil Oil, Geranium Oil, Rosemary Oil and Fragrance",
        storage = "None",
        category_id = 3
    )
    Styling_gel = Product(
        name = "Locced-In Styling Gel",
        price = 14.99,
        quantity = 50,
        e_pitch = "Imagine a Gel that work's for all Hair style's and holds your hair firmly, regardless of Profession. Of course it's made Ethically or ethically Sourced",
        description = "Naturally sourced styling gel designed for a Range of Hair from Easy to Hold and resistant Hard to Hold Hair. Maintains locks, twists, braids and other naturals styles all types of hair. Holds resistant, color, treated and grey hair. No flaking, no build up, no alcohol. Defines natural hair pattern. Did we mention it's tropical scented? ",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
        image_2 = None,
        background = None,
        application = "Wash and condition Hair. Get preparation's for Styling add gel as you apply style.",
        ingredients = "Water, Carbomer, Triethanolamine, Soy Bean Oil, VP/DMAPA and Acrylates Copolymer Styrene/Acrylate Copolymer, Yarrow Roots Extract, Rosemary Extract, Nettle Extract, Capryloyl Glycol Phenoxyethanol, Fragrance",
        storage = "Keep in cool & non-humid Area.",
        category_id = 5
    )
    Hair_growth_oil = Product(
        name = "Bold Growth Oil",
        price = 44.99,
        quantity = 100,
        e_pitch = "No Gimmicks, just natural product backed by science that actually work and happen to smell good.",
        description = "Male pattern badness is a real thing alot majority of men suffer from it in some form, wether it be in your face or starting to persist and yes we know you used to have a beautiful full head of hair in you 20's but to restore that scalp right now to that legally draftable glory try our Follicle Stimulating, DHT Blocking, Hair growth tested-oil formula, to achieve the fastest and heathiest hair growth possible. Sustainably hand blended and has regrown Hair of All types and all genders also promotes excelled hair growth.  ",
        image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/HairGrowth/Hair_Growth_Oils.png",
        image_2 = None ,
        background = None,
        application = "Apply 3 times a week before washing, Use our BoldSkin Shampoo & cleanse scalp",
        ingredients = " jojoba oil, Rosemary oil, Green Coffee Bean Oil, peppermint oil, Pumpkin Seed oil, Argan Oil, Tea Tree Oil, Lavendar Oil ",
        storage = "Store in cool Dry place and Keep away from Sunlight",
        category_id = 5
    )
    # Add A Styling Wax (For harder sweater's)
    # Style_shine_spray = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Face_Scrub = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Face_Moisturizer = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Beard_Wash = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Beard_Balm = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Beard_Exfoilater = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Body_Wash = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Body_Scrub = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Scalp_Mositurizer = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",
    # )
    # Scalp_Scrub = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",        
    # )
    # Curl_Conditioner = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",        
    # )
    # Leave_in_Conditioner = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",        
    # )
    # Bold_Shampoo = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",        
    # )
    # Bold_moisturizer  = Product(
    #     name = "",
    #     price = "",
    #     quantity = "",
    #     e_pitch = "",
    #     description = "",
    #     image_1 = "https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/testbranch/assets/Products/BoldSkin/ComingSoon.png",
    #     image_2 = None,
    #     background = None,
    #     application = "",
    #     ingredients = "",
    #     storage = "",        
    # )
    db.session.add_all([
        BeigeJogger,
        SummerJogger,
        WhiteT,
        BlackT,
        LightGreyT,
        WavyCurlComb,
        TightCurlComb,
        FineComb,
        MediumComb,
        ThickComb,
        SoftBristleBrush,
        HardBristleBrush,
        FeelGoodLotion,
        
        Smell_good_deodorant,
        Styling_gel,
        Hair_growth_oil,
        
        # Style_shine_spray,
        # Face_Scrub,
        # Face_Moisturizer,
        # Beard_Wash,
        # Body_Wash,
        # Body_Scrub,
        # Scalp_Mositurizer,
        # Scalp_Scrub,
        # Curl_Conditioner,
        # Leave_in_Conditioner,
        # Bold_Shampoo,
        # Bold_moisturizer
    ])
    db.session.commit()
    
# def declare_users():
    # db.session.query(User).delete()
#     # Not populating
#     admin = User(
#         username = "BigDaddyK",
#         name = "big bread",
#         email = "bread@gmail.com",
#         password = "bread"
#     )
#     db.session.add(admin)
    # db.session.commit()

def declare_order_status():
    db.session.query(OrderStatus).delete()
    ordered = OrderStatus(
        status= "Ordered"
    )
    in_transit = OrderStatus(
        status= "In Transit"
    )
    delivered = OrderStatus(
        status = "Delivered"
    )
    db.session.add_all([ordered, in_transit, delivered])
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        
        declare_categories()
        declare_products()
        declare_order_status()
        # declare_users()
        

# def clear_tables():
    # db.session.query(User).delete()
#     db.session.query(Cart).delete()
    # db.session.commit()
    



