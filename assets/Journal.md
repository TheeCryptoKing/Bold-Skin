# Project Journal 
<!-- Kwame Notes -->
<!-- Can use for one line break in sentences <li></li>, <br></br>, and <pre></pre> -->
<!-- Can use <p></p> tags to create newline and space between lines -->
<!-- <textarea></textarea> Opening text box -->
<!-- <span></span> and <style></style> for styling or id's and Class names-->


<p>

- MVP <br>
Products <br>
CAtegories <br>
Order <br>
OrderItems <br>
User <br>
Cart <br>
CartItems <br>

- Advanced <br>
Payments <br>
Reviews <br>
Comments <br>
addresses <br>

- Develop Backend <br>
MVP Status: W.I.P.<br>
<ol>
<li>Create Models with serialize rules, Validation, Regex if you want **Properly</li>
<li>Create Seed Data(Fix any Logic errors)</li>
<li>Create All Api Routes needed</li>
<li>Enable Flask Login(troubeshoot)</li>
<li>Use .csv files or PICKL (or both)</li>
<li>Have All API routes working and retrieveing formatted data before moving foward</li>
<li>Punch in Faker/Placeholder Data for Tables for what we don't have</li>
<li>hash Passwors except main admin</li>
</ol>

- Develop Frontend grid and base style(HTML grid)<br>
MVP Status: W.I.P.<br>
<ol>
<li>Practice Flexgrid and Flex and slight padding around</li>
<li>Enable Yup and Formik</li>
<li>Try to do in basic CSS, choose 2 different UI library(TailwindCSS & BootStrapCss(install most likely))</li>
<li>Pracitce JSX and scripts</li>
<li>Finish Basic Styling then Start incorporating backend linking buttons and Forms</li>
<li>Modal for add to cart or side modal</li>
<li>S.N. Bootstrap preferred for nav.link(ReactRouter Feature)</li>
</ol>

- Connect backend and frontend()<br>
MVP Status: W.I.P.<br>
<ol>
<li>Connect and add all routes to methods and forms</li>
<li>Enable Sign in Necessity for Purchase</li>
<li>Enable</li>
</ol>

- Advanced Deliverables<br>
Advanced Status: Start after MVP<br>
<ol>
<li>Shop by Products(Hair, Face, Beard, Body)</li>
<li>Product, recommendations based on order history</li>
<li>Filter Search by initiative</li>
<li>Admin Feature with added Role Table</li>
<li>Create Google Login</li>
<li>Create Google tracking location to Give Approximate time for Package Delivery</li>
<li>3d/Chatgpt Avatar creation</li>
<li>Enable Amazon s3 storing for blob data fro images</li>
<li>Rewrite Backend in Rust</li>
<li>Rewrite Front end in Next.js</li>
</ol>
</p>



- Kwame Log<br>
Creating Tables<br> 
All base data created, Relationships next<br>
Populated categories, products, Need to write serializers, validations, flasklogin parameters, API routes, bcrypt, and password hash  <br>


<!-- ######################## Bold-Skin Product's  ######

key : value pair for icons

bootstrap jumbotron & install & link bootstrap in app.jsx

Product Intiative Column, with intiatives
fetch data and .split string at commas and do comparison of the string value 
set value equal to icon image
In frontend use <p> for image and post text next to it. Flex box 
write function of front end to add icon
key = intiative
value = 


Details: 
Skin: vitamin D, for Vitamin E. For all skin types, including sensitive skin. Clean, vegan, gluten-free , earth-conscious, & sustainable.
Hair Scalp: For all Hair/Scalp types, including sensitive scalps. Clean, vegan, gluten-free earth-conscious, & sustainable.
Scrubs: Powered by AHAs, fruit enzymes and sugar, this triple action scrub
Face & Beard: 
Body:  

How to Use(Accordion?) idk how i feel about it

#####################
##### Blueprint #####
#####################
############################### MAIN DISPLAY 
# name: Bold Beard Balm (Right)
# images: Beard Moisturizer (Left[ALL IMAGES])
# price: 24.99 (Right)
# quantity: 50 (Right)
# initiative: 
Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic, Vegan & Naturally Sourced

############################### DETAILS DISPLAY
# Elevator Pitch/One word description:
"
Think of a Product that makes your beard turn heads, a moisturizer that makes you beard as shiny as the diamonds on your jewelry. 
"
# description2: 
"
Find out how great your beard can look. When you use our Bold Beard Balm to shape, smooth and define facial hair. Beard hair should be moisturized regularly to foster growth. Our beard balm works on beards of all types, from loose and wavy Easy-to-tame beards and it's especially great for Hard-to-tame beards that require a bit of taming before you head out. It seal's lasting & nourishing moisture in using tested vegan & oils. Bold Beard-Balm requires little amounts for use, all while having a very consistent spread. Bold Beard-Balm has dense and tacky consistency, which is a big assist when it comes to shaping and defining your beard look. We Know You will Love it! 
"
# Application: 
"
Use a Bold Comb and Apply to Already Lightly combed and wet beard
"
# storage: 
" Store in Cool-dry Area " 

############################# INGREDIENTS DISPLAY 
# ingredients: 
Castor Seed Oil, Shea Butter, Grape Seed oil, Candelilla Wax, Coconut oil, Carnauba Wax, Hydrogenated Castor oil, Passion Fruit Seed Oil, Argan Kernel Oil, Tea Tree Leaf Oil, Palm oil, Omega-3 oils, Fragrance 


###### Done #####

# name: "BoldSkin Wavy Curl Comb" (Zebra and Black)
# images: 3a "Black" Comb, 3a "Zebra" Comb 
# price: 24.99
# quantity: 50
# initiative: 
Recyclebale, Non-comedogenic, Non-carcogenic, Cruelty-free, Vegan & Naturally Sourced
# Elevator Pitch: 
"
Imagine a looking at a person with gorgeous hair and they pull out this stylish comb and you can't stop staring because you don't know which looks better, now imagine your that person being stared at is you. 
"
# description:
"
Comb designed to help get those wavy curls mositurized, untangled and ready for events of all types. 
" 
# ingredients: Contains Recylced Materials, Non-Carcengonic ink 
# storage: "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time" 

# name: "3c Bold Comb" 
# images: 3c comb Front, 3c comb Back  
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# Elevator pitch:
"Think of a 3c comb that doesn't pull on your scalp and make you go to bed with a tender scalp and is ethically sourced"
# description: 
"
Comb designed to help mositurize and get threw those tight curls in a easy and painless way , untangled and ready for events of all types
"
# ingredients: Contains Recylced Materials, Non-Carcengonic ink 
# storage: "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time"


# name: BoldSkin Soft Brush
# image: Bamboo "Soft" Bristle Brushes
# price: 24.99
# quantity: 50
# Elevator Pitch:
" Ethically Sourced, durable, sustainable, and pocketable high-quality soft bristle brush "
# description: 
"
Made out of the strongest and sustainable Wood on the planet, Recylcled-Bamboo, Paired with thousands of Non-Cruelty, Boar-Bristle Brushes. Boar-bristle brushes are know for their exceptional smoothing and shine-enhancing abilities. Built to last and built to apply the last brushes needed on any wave stlye
"
# initiative: 
Contains Recylced Materials, Recyclebale, Non-carcogenic, Vegan & Cruelty free, Personal Care, Clean & Naturally Derived
# ingredients: Cleanly-sourced and Reused-Bamboo, Cruelty-free Boar-Bristle Brushes
# storage: 
"Regularly clean bristles every 3 months.
Do not soak or leave wood in Water for long perids of Time"


############### Jogger sets 
# name: "BoldSkin" jogger set (Beige)
# images: Beige Jogger (Front and Back)
# price: 89.99
# quantity: 50
# Elevator Pitch: 
"A Cozy Slip-in Jogger made from recycled and ethically sourced cotton, that you will never want to take off. Oh did i mention it look's really good on you To?"
# description: 
"
Created in a cruelty free enviornment and made from ethically and reycled sourced cotton and hemp. 
A stylish and concious way to end the Fast Fashion Trend that is slowly killling our planet. 
"
# initiative: 
Gluten-Free, Contains Recylced and Cruelty Free Cotton, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: Cotton & hemp
# storage: 
Wash on Slow, on cold and Warm and Please AirDry


############################ Make T-shirt Route with options
# Images: LightGrey_T(Front and Back)
# name: BoldSkin Grey T-shirt
# description: 
"
Created in a cruelty free enviornment and made from ethically and reycled sourced cotton and hemp. 
A stylish and concious way to end the Fast Fashion Trend that is slowly killling our planet. 
"
# price: 34.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic, Cruelty-free, Vegan & Naturaly Sourced 
# ingredients: Cotton & hemp
# storage: 
Wash on Slow, on cold and Warm and Please AirDry

# Images: White_T(Front and Back)
# name: BoldSkin White T-shirt
# price: 27.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic, Cruelty-free, Vegan & Naturaly Sourced 
# description: 
"
Created in a cruelty free enviornment and made from ethically and reycled sourced cotton and hemp. 
A stylish and concious way to end the Fast Fashion Trend that is slowly killling our planet. 
"
# ingredients: 
Gluten-Free, Contains Recylced and Cruelty Free Cotton, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: Cotton & hemp
# storage: 
Wash on Slow, on cold and Warm and Please AirDry

# name: BoldSkin Black T-shirt
# Images: Black_T(Front and Back)
# price: 29.99
# quantity: 50
# initiative: Contains Recylced and Cruelty Free Cotton, Recyclebale, Non-comedogenic, Non-carcogenic, Cruelty-free, Vegan & Naturaly Sourced 
# description: 
"
Created in a cruelty free enviornment and made from ethically and reycled sourced cotton and hemp. 
A stylish and concious way to end the Fast Fashion Trend that is slowly killling our planet. 
"
# ingredients: Cotton & hemp
# storage: 
Wash on Slow, on cold and Warm and Please AirDry

################################# Loc's 
# name: Locced-In Styling Gel 
# Images: Loc's/Braid Styling Gel (mango scented)
# price: 14.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic, Cruelty-free, Vegan & Naturaly Sourced 
# description: 
"
Naturally sourced loc gel designed for resistant and Hard to Hold Locks and Hair. Maintains locks, twists and naturals. Holds resistant, color, treated and grey hair. No flaking, no build up, no alcohol. Defines natural curl pattern.
" 
# application :
" Wash and condition Hair. Get prepartion's for Styling add gel as you apply style."
# ingredients:  
Water, Carbomer, Triethanolamine, Soy Bean Oil, VP/DMAPA and Acrylates Copolymer Styrene/Acrylate Copolymer, Yarrow Roots Extract, Rosemary Extract, Nettle Extract, Caprylyl Glycol Phenoxyethanol, Fragrance
# storage:
keep in cool & non-humid Area. 

# name: Smell Good Lotion(or Butter )
# Images: Body fragranced lotion (3 different types)
# price: 19.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic, Cruelty-free, Vegan & Naturaly Sourced 
# Elevator Pitch: ""
# description: 
"
Made with all skin type's in mind, oily, coarse, soft, and sensitive. Apply across body and watch the magic happen as you skin get's a Deep hydration and and noursihment. Made with skin revitalization in mind. Fragrance and nourish your body with this curated whipped Smell Good lotion loaded with nearly 25% rich butters and restorative tropical oils and extracts.
As men we have a teendency to get up and Go but after 1-3 application's of this butter, your partner and your skin will thank you and we highly expect you to become a returning customer!
"
# appliation: 
for best result when applied to damp skin

# ingredients:
Kalahari Melon oil, Sorrel oil, Baobab oil, Sunflower oil, Rice Bran oil, Coconut oil, Jojoba oil, Shea Butter, Mango butter, Frangrance
# storage: 
Store in a low humid & cool Dry Place 

# name: Feel Good Deodorant
# Images: Deodorant (3 different scents)(Bourbon, Palm Tree, PlayMaker)
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# price: 14.99
# quantity: 50
# Elevator Pitch: ""
# description: 
"
Smell good and forget the things that make you stress with out Feel Good Deodorant made with sustainability in mind and 99% plastic free. Our high-performance formula is naturally derived, clean, vegan & dermatologist-tested—formulated without parabens, phthalates and silicones. Our nature-inspired scents are bold, fresh, memorable and created with upcycled ingredients and essential oils. Made for all type's of men wether it's All day constructuion or desk work. Your partner will thank you, and your Mom will ask "What are you wearing? Smells Good. Guaranteed." 
"
# ingredients: Hemp, Coconut oil, Rosemary Extract, Arrowroot Powder, Shea Butter, Sunflower Seed Wax, Candelilla Wax, (Rosemary) Flower Extract, Soybean oil, Lavandin Oil, Basil Oil, Geranium Oil, Rosemary Oil and Fragrance
# storage:
 
# name: Hair growth oil
# Images: Hair Growth oil
# price: 
# quantity: 50
# Elevator Pitch: 
""
# description: 
"
Male pattern badness is a real thing alot majority of men suffer from it in some form, wether it be in your face or starting to persist and yes you used to have a beautiful full head of hair in you 20's but to restore that scalp right now to that legally draftable glory try our Follicle Stimulating, DHT Blocking, Hair growth tested-oil formula, to achieve the fastest and heathiest hair growth possible. Sustainably hand blended and has regrown Hair of ALl types and all genders also promotes excelled hair growth.   
"
# application: "Apply 3 times a week before washing, Use our BoldSkin Shampoo & cleanse scalp"
# Roller once a week to stimulate your follicles.
# Use our Shmapoo and CLeanse your scalp
# initiative: Gluten-Free, Recyclebale, Non-comedogenic, Non-carcogenic, Vegan, Cruelty Free & Ethically Sourced 
# ingredients:
jojoba oil, Rosemary oil, Green Coffee Bean Oil, peppermint oil, Pumpkin Seed oil, Argan Oil, Tea Tree Oil, Lavendar Oil   
# storage: 
Store in cool Dry place and Keep away from Sunlight 

# HAIR GROWTH SCIENCE(Actually Real)
Researchers found in this study, which compared Rosemary Oil to Minoxidil (the active ingredient in Rogaine) that the natural remedy was just as effective OTC drug. Caffeine can help decrease DHT and increase growth factors as shown in this study. In another study they even boldly state in their title that "Peppermint Oil Promotes Hair Growth Without Toxic Signs"! There was even a randomized double blind trial that showedlavender, rosemary, thyme, cedarwood  essential oils to be a safe and effective treatment of Alopecia Areata! Pumpkin seed oil can help reduce DHT and the study shows that it “provides evidence of a promising potential role of PSO in treating Female Pattern Hair Loss”. This shows us that natural remedies can be just as effective than the OTC in helping to promote hair growth and prevent hair loss!

############### Needed Products 
# images: Bold Scalp Conditioner 
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Bold Scalp exfoiliater 
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Bold Face Scrub
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50 
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Bold Face Exfoiliater
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Bold Face Moisturizer
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Beard Wash
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Beard Exfoilater
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:


# images: Bold Skin Scrub
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Bold Skin Wash 
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

###########################
### ME BEING SUPER EXTRA ##
###########################
# images: Bold Skin Bluetooth Clippers 
# images: Bold Skin Razer
# images: Bold SKin Shaving Gel
# images: Acv rinse
# images: beard balm
# images: Scalp exfoilater (For troublesome or oily scalps)

# images: Comb (Thick, Fine, Medium)
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Summer grey jogger set
# name: BoldSkin Summer set
# description: 
# price: 59.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Bold Man's Comb (fine & Bold) 
# name: " "BoldSkin" Comb" (Card for each Type or Dropdown )
# description: 
"
 Comb hust ethically Sorced 
"
# price: 19.99
# quantity: 50
# initiative: 
Contains Recylced Materials, Recyclebale, Non-carcogenic, Vegan & Cruelty free, Personal Care, Clean & Naturally Derived
# ingredients: 
# storage: "Please do not drop boiling water or store in Heavy Sunlight for Extended Periods at a time"

# images: Loc's Moisturizer
# name: Loc 
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Loc's scalp oil (hair growth oil)
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Loc's Shiner
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Hair pins (For styling???)
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# images: Concealer per skin color (create skin palettes for site) (Unsure)
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients: 
# storage:

# image: Hard Bristle Brushes (Needed)
# name: BoldSkin Hard Brush
# description: 
# price: 24.99
# quantity: 50
# initiative: Gluten-Free, Contains Recylced Materials, Recyclebale, Non-comedogenic, Non-carcogenic
# ingredients:
# storage: 
  -->